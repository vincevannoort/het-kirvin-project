"use client"

import temperature_per_station from '@/data/temperature_per_station.json'
import temperature_per_day from '@/data/temperature_per_day.json'
import Highcharts, { SeriesLineOptions, SeriesOptionsType } from 'highcharts'
import HighchartsReact from 'highcharts-react-official'


export default function TemperaturePerStation() {


    let series: Array<SeriesLineOptions> = [
        // create line for average
        {
            type: "line",
            opacity: 1,
            dashStyle: "LongDash",
            lineWidth: 1,
            color: 'blue',
            zIndex: 100,
            name: 'Average',
            data: temperature_per_day.map(d => [d.date, d.temperature]),
        },
        // append lines for each station (first five)
        ...temperature_per_station.slice(0, 5).map(stationData => {
            return {
                type: "line",
                opacity: 0.5,
                name: 'Station ' + stationData.station,
                data: stationData.data.map(d => [d.date, d.temperature])
            }
        }) as Array<SeriesLineOptions>
    ]

    const options: Highcharts.Options = {
        title: {
            text: 'Temperature per day',
        },
        tooltip: {
            shared: true
        },
        subtitle: {
            text: 'Example',
        },
        yAxis: {
            title: {
                text: 'Temperature'
            }
        },
        xAxis: {
            type: 'datetime',
            title: {
                text: 'Day'
            }
        },
        series: series
    }

    return (
        <div>
            <HighchartsReact
                highcharts={Highcharts}
                options={options}
            />
        </div>
    )
}