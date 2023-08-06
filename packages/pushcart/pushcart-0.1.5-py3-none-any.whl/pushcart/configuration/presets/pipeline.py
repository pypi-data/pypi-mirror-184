if __package__:
    from pushcart import spark

pipeline_name = spark.conf.get("pushcart.pipelineName")
