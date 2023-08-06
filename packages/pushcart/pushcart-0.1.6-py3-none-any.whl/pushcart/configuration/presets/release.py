import csv
import json
import os
from glob import glob
from pathlib import Path

import tomli
import yaml
from traitlets.config.application import get_config

from pushcart.release import Release

user = Release.instance().user
repo = Release.instance().repo
log = Release.instance().log

loaders = {".json": json.load, ".toml": tomli.load, ".yaml": yaml.load}

# TODO: See if the /Workspace/Repos part cannot be inferred or parameterized

all_pipelines_dir = f"/Workspace/Repos/{user}/{repo}/pipelines"
log.debug(f"Pulling pipeline configuration files from {all_pipelines_dir}")


def __enrich_sources_config(pipeline_name: str, config_sources: list) -> list:
    sources = []

    for s in config_sources:
        source_dict = s

        if isinstance(s.get("params"), dict):
            source_dict["params"] = json.dumps(s["params"])
        sources.append(source_dict)

    return sources


def __enrich_transformations_config(
    pipeline_name: str, config_transformations: list
) -> list:
    transformations = []

    for t in config_transformations:
        if t.get("config"):
            with open(
                os.path.join(all_pipelines_dir, pipeline_name, t["config"]), "r"
            ) as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    for k, v in row.items():
                        if k == "column_order":
                            row[k] = int(v) if len(v) > 0 else None
                        elif k == "not_null":
                            row[k] = bool(v) if len(v) > 0 else None

                    row["from"] = t["from"]
                    row["into"] = t["into"]

                    transformations.append(row)

        else:
            transformations.append(t)

    return transformations


def __enrich_destinations_config(pipeline_name: str, config_destinations: list) -> list:
    return config_destinations


def __enrich_pipeline_config(pipeline_name: str, config_dict: dict) -> dict:
    enriched_config_dict = {}

    enrichment_func = {
        "sources": __enrich_sources_config,
        "transformations": __enrich_transformations_config,
        "destinations": __enrich_destinations_config,
    }

    for stage_name in ["sources", "transformations", "destinations"]:
        stage = config_dict.get(stage_name, [])

        stage = enrichment_func[stage_name](pipeline_name, stage)
        stage = [{k: None if v == "" else v for k, v in elem.items()} for elem in stage]

        for stage_element in stage:
            stage_element["pipeline_name"] = pipeline_name

        enriched_config_dict[stage_name] = stage

    return enriched_config_dict


def __load_config_file(config_file_path: str) -> dict:
    config_dict = {}

    with open(config_file_path, "r") as config_file:
        ext = Path(config_file_path).suffix
        config_dict = loaders[ext](config_file)

    return config_dict


def collect_cluster_configs(pipeline_names: list) -> list:
    log.info("Collected cluster configurations for pipelines:")

    cluster_configs_dir = os.path.join(Path(all_pipelines_dir).parent, "clusters")

    cluster_configs = []
    for p in pipeline_names:
        all_cluster_config_files = set(glob(f"{cluster_configs_dir}/*"))

        search_for_files = [
            os.path.join(cluster_configs_dir, f"{p}{ext}") for ext in loaders.keys()
        ]

        found_cluster_configs = all_cluster_config_files.intersection(search_for_files)
        first_match = found_cluster_configs.pop()

        if found_cluster_configs:
            log.warning(
                f"Found more than one potential cluster configuration for {p}. Choosing {first_match}"
            )

        cluster_configs.append({p: __load_config_file(first_match)})
        log.info(f"- {p}")

    if not cluster_configs:
        log.info("- None")

    return cluster_configs


def collect_pipeline_configs(pipelines_dir: str) -> list:
    pipeline_configs = []
    pipeline_files = []

    json_files = glob(f"{pipelines_dir}/**/*.json")
    pipeline_files.extend(json_files)
    if json_files:
        log.info(f"Found {len(json_files)} JSON files")

    toml_files = glob(f"{pipelines_dir}/**/*.toml")
    pipeline_files.extend(toml_files)
    if toml_files:
        log.info(f"Found {len(toml_files)} TOML files")

    yaml_files = glob(f"{pipelines_dir}/**/*.yaml")
    pipeline_files.extend(yaml_files)
    if yaml_files:
        log.info(f"Found {len(yaml_files)} YAML files")

    pipeline_names = set()
    for config_file_path in pipeline_files:
        pipeline_name = Path(config_file_path).parent.stem
        pipeline_names.add(pipeline_name)

        config_dict = __enrich_pipeline_config(
            pipeline_name, __load_config_file(config_file_path)
        )
        pipeline_configs.append(config_dict)

    cluster_configs = collect_cluster_configs(pipeline_names)

    stage_records = {
        "clusters": [],
        "sources": [],
        "transformations": [],
        "destinations": [],
    }

    stage_records["clusters"] = cluster_configs

    for config in pipeline_configs:
        for stage_name, stage in config.items():
            stage_records[stage_name].extend(stage)

    if stage_records["clusters"]:
        log.info(f"Loaded {len(stage_records['clusters'])} cluster configurations")
    if stage_records["sources"]:
        log.info(f"Loaded {len(stage_records['sources'])} sources")
    if stage_records["transformations"]:
        log.info(f"Loaded {len(stage_records['transformations'])} transformations")
    if stage_records["destinations"]:
        log.info(f"Loaded {len(stage_records['destinations'])} destinations")

    return stage_records


p = collect_pipeline_configs(all_pipelines_dir)
c = get_config()

for stage_name, stage in p.items():
    setattr(c.PipelineConfiguration, stage_name, stage)
