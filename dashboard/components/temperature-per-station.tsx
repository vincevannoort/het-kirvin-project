"use client"

import temperature_per_station from '@/data/temperature_per_station.json'
import temperature_per_day from '@/data/temperature_per_day.json'
import Highcharts, { SeriesLineOptions, SeriesOptionsType } from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import { timestamp_within_date_range, useDateRangeStore } from './date-range-picker'


export default function TemperaturePerStation() {
    // retrieve date range from store (automatically updated by date range picker)
    const { dateRange } = useDateRangeStore();

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
            data: (
                temperature_per_day
                    // only keep dates within date range
                    .filter(row => timestamp_within_date_range(row.date, dateRange))
                    // map to required input format
                    .map(row => [row.date, row.temperature])
            ),
        },
        // append lines for each station (first five)
        ...temperature_per_station.slice(0, 5).map(stationData => {
            return {
                type: "line",
                opacity: 0.5,
                name: 'Station ' + stationData.station,
                data: (
                    stationData.data
                        // only keep dates within date range
                        .filter(row => timestamp_within_date_range(row.date, dateRange))
                        // map to required input format
                        .map(row => [row.date, row.temperature])
                )
            }
        }) as Array<SeriesLineOptions>
    ]

    const options: Highcharts.Options = {
        title: {
            text: 'Temperature per day',
        },
        tooltip: {
            shared: true,
            valueSuffix: "°",
        },
        yAxis: {
            title: {
                text: 'Temperature'
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