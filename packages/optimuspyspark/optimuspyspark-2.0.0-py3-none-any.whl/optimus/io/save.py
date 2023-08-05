from pyspark.sql import DataFrame

from optimus.helpers.decorators import *


def save(self):
    @add_attr(save)
    def json(path_name, mode ="overwrite", num_partitions=1):
        """
        Save data frame in a json file
        :param path_name:
        :param num_partitions:
        :return:
        """
        assert isinstance(path_name, str), "Error: path must be a string"
        assert (num_partitions <= self.rdd.getNumPartitions()), "Error: num_partitions specified is greater that the" \
                                                                "partitions in file store in memory."
        self.repartition(num_partitions).write.format("json").mode(mode).save(path_name)

        # os.chdir(path_name + "/")
        # for file in glob.glob("*.json"):
        #    shutil.copyfile(file, path_name)

        # shutil.copyfile(path_name+ "")
        # shutil.rmtree("/folder_name")

    # TODO: Check this to save to a single file
    @add_attr(save)
    def csv(path_name, header="true", mode="overwrite", sep=",", num_partitions=1):
        """
        Save data frame to a CSV file.
        :param path_name: Path to write the DF and the name of the output CSV file.
        :param header: True or False to include header
        :param mode: Specifies the behavior of the save operation when data already exists.
                    "append": Append contents of this DataFrame to existing data.
                    "overwrite" (default case): Overwrite existing data.
                    "ignore": Silently ignore this operation if data already exists.
                    "error": Throw an exception if data already exists.
        :param sep: sets the single character as a separator for each field and value. If None is set,
        it uses the default value.
        :param num_partitions:
        :return: Dataframe in a CSV format in the specified path.
        """

        assert isinstance(path_name, str), "Error: path must be a string"
        assert (num_partitions <= self.rdd.getNumPartitions()), "Error: num_partitions specified is greater that the" \
                                                                "partitions in file store in memory."
        assert header == "true" or header == "false", "Error header must be 'true' or 'false'"

        if header == "true":
            header = True
        else:
            header = False

        self.repartition(1).write.options(header=header).mode(mode).csv(path_name, sep=sep)
        # shutil.rmtree("/folder_name")

    @add_attr(save)
    def parquet(path_name, num_partitions=1):
        """
        Save data frame to a parquet file
        :param path_name:
        :param num_partitions:
        :return:
        """
        assert isinstance(path_name, str), "Error: path must be a string"
        assert (num_partitions <= self.rdd.getNumPartitions()), "Error: num_partitions specified is greater that the" \
                                                                "partitions in file store in memory."
        self.coalesce(num_partitions).write.parquet(path_name)

    return save


DataFrame.save = property(save)
