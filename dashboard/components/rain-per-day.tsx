"use client"

import rain_per_day from '@/data/rain_per_day.json'
import Highcharts, { SeriesLineOptions, SeriesScatterOptions } from 'highcharts'
import HighchartsReact from 'highcharts-react-official'

export function RainPerDay() {

    // Highcharts.seriesTypes.scatter.prototype.noSharedTooltip = false;

    let series: Array<SeriesLineOptions | SeriesScatterOptions> = [
        {
            type: "line",
            name: '7-day moving average',
            lineWidth: 2,
            color: 'blue',
            data: rain_per_day.map(row => [row.date, row.rollmean]),
        }, {
            type: "scatter",
            opacity: 0.5,
            name: 'average',
            marker: {
                symbol: 'circle'
            },
            color: 'blue',
            data: rain_per_day.map(row => [row.date, row.rainfall_amount]),
        }
    ]

    const options: Highcharts.Options = {
        title: {
            text: 'Rain per day',
        },
        tooltip: {
            shared: true,
            valueSuffix: " mm",
        },
        yAxis: {
            title: {
                text: ''
            },
            labels: {
                format: '{value} mm'
            }
        },
        xAxis: {
            type: 'datetime',
            crosshair: true
        },
        // plotOptions: {
        //     scatter: {
        //         tooltip: {
        //             format: "average"
        //         }
        //     }
        // },
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