"""Set of classes to prepare objects for knowledge"""


class FormatText():
    """Class to prepare object of Format KnowledgeDataType"""

    def __init__(self, value, **kwargs):
        """ Initializing the FormatText object

        Args:
            value: value to write to knowledge,
            **kwargs: oprional keyword arguments for Format KnowledgeDataType:
                pipe: Angular pipe name,
                args: Angular pipe parameters,
                prefix: prefix,
                suffix: suffix
                color: name of color

        Returns:
            String to use for Format KnowledgeDataType

        Example:
            FormatText('1995-12-17T03:24:00', pipe='DatePipe', args='fullDate', prefix='Dzisiaj jest', suffix='dzien', color='red')
        """

        self.kwargs = kwargs
        self.kwargs['value'] = value
        self.__str__()

    def __str__(self):
        """ Change to proper string """

        return str(self.kwargs).replace("'", '"')


class FormatChart():
    """Class to prepare object of chart KnowledgeDataType

    Args:
            chart_type: type of chart to create,
            module: name of module,
            variable: name of variable to plot,
            start_time: start time of chart range,
            stop_time: stop time of chart range,
            source: name of table in ClickHouse,

        Returns:
            String to use for Chart KnowledgeDataType

        Example:
            FormatChart('timeseries', 'Socomec', 'P', '2021-12-17T03:00:00Z', '2021-12-17T05:00:00Z')
        """

    def __init__(self, chart_type, module, variable, start_time, stop_time, source):
        self.chart_type = chart_type
        self.module = module
        self.variable = variable
        self.start_time = start_time
        self.stop_time = stop_time
        self.source = source

        self.__str__()

    def __str__(self):
        value = f'''{{"chartType":"{self.chart_type}","properties":{{"module":"{self.module}","variable":"{self.variable}","startTime":"{self.start_time}","endTime":"{self.stop_time}","source":"{self.source}"}}}}'''
        return value
