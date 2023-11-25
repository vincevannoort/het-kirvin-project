"use client"

import sunshine_per_day from '@/data/sunshine_per_day.json'
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
            name: 'Average (7d)',
            data: sunshine_per_day.map(d => [d.date, d.sunshine_duration]),
        },
    ]

    const options: Highcharts.Options = {
        title: {
            text: 'Sunshine per day',
        },
        tooltip: {
            shared: true,
            valueSuffix: " hours",
        },
        yAxis: {
            title: {
                text: 'Sunshine duration in hours'
            }
        },
        xAxis: {
            type: 'datetime',
            crosshair: true,
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