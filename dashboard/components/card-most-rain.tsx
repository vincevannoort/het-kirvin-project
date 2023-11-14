import most_rainfall from '@/data/most_rainfall.json'
import React from "react";
import { CardWithValue } from './card-with-value';


export function CardMostRain() {

    const most_rainfall_day = most_rainfall.reduce(function (prev, current) {
        return (prev && prev.max_rainfall_amount > current.max_rainfall_amount) ? prev : current
    })

    return (
        <CardWithValue
            title={'Most rainfall'}
            date={most_rainfall_day.date}
            value_type={'Rainfall'}
            value={most_rainfall_day.max_rainfall_amount}
            station={most_rainfall_day.station ? most_rainfall_day.station : 'unknown'}
        />
    )
}