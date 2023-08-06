class Spark:
  def __init__(self):
    self.spark = SparkSession.builder\
                .appName("BaseEnriquecida")\
                .enableHiveSupport()\
                .config("spark.yarn.executor.memoryOverhead","4G")\
                .config("spark.executor.memory", "12G")\
                .config("spark.dynamicAllocation.enabled", "true")\
                .config("spark.dynamicAllocation.initialExecutors", "2")\
                .config("spark.dynamicAllocation.maxExecutors","5")\
                .config("spark.executor.cores", "8")\
                .config("spark.cores.max", "3")\
                .config("spark.driver.memory", "4G")\
                .config("spark.ui.killEnabled", "true")\
                .getOrCreate()
    
    self.sqlContext = SQLContext(spark)
  
  def getSpark():
    return self.spark
  
  def getSqlContext():
    return self.sqlContext