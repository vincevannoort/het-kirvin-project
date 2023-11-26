"use client"

import sunshine_per_day from '@/data/sunshine_per_day.json'
import Highcharts, { SeriesLineOptions, SeriesOptionsType } from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import { timestamp_within_date_range, useDateRangeStore } from './date-range-picker';


export default function TemperaturePerStation() {
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
            data: sunshine_per_day
                // only keep dates within date range
                .filter(row => timestamp_within_date_range(row.date, dateRange))
                // map to required input format
                .map(d => [d.date, d.sunshine_duration]),
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