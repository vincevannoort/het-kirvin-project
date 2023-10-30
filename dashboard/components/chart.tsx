"use client"

import styles from './page.module.css'
import { LineChart, XAxis, Tooltip, CartesianGrid, Line, YAxis, ResponsiveContainer, ReferenceLine } from 'recharts'
import data from '../data/temperature_per_day.json'
import { useState } from 'react'
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'


export default function Chart() {
    const options = {
        title: {
            text: 'Temperature per day'
        },
        series: [{
            data: data.map(o => {
                return [Date.parse(o.date), o.temperature]
            })
        }],
        xAxis: {
            type: 'datetime'
        },
    }
    const [interval, setInterval] = useState(7)
    return (
        <div>
            <h1>Temperature per day</h1>
            <ResponsiveContainer width="100%" height={350}>
                <LineChart data={data} margin={{ top: 5, right: 20, left: 10, bottom: 50 }}>
                    <XAxis dataKey="date" angle={-45} textAnchor="end" interval="preserveStartEnd" />
                    <YAxis dataKey="temperature" />
                    <Tooltip />
                    <CartesianGrid stroke="#f5f5f5" />
                    <Line dataKey="temperature" stroke="#14a8f7" dot={false} />
                    <ReferenceLine y={0} label="Freezing point" />
                </LineChart>
            </ResponsiveContainer>
            <br />
            <button onClick={() => { setInterval(interval + 1) }}>increase interval</button>
            <hr />
            <HighchartsReact
                highcharts={Highcharts}
                options={options}
            />
        </div>
    )
}
