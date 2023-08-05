try:
    import influxdb
except:
    pass


def write_softsensor(self, puntcode, testcode, analyte, value):

    influx_json = []
    
    influx_json.append({
        "measurement": puntcode,
        "tags": {
            "testcode": testcode,
            "analyte": analyte
            },
        "fields": {
            "value": value
            }
        })

    client = influxdb.InfluxDBClient(database='slimm')
    client.write_points(influx_json)
