import max_temperature from '@/data/max_temperature.json'
import React from "react";
import { CardWithValue } from './card-with-value';


export default function CardMaxTemperature() {

    const max_temperature_day = max_temperature.reduce(function (prev, current) {
        return (prev && prev.max_temperature > current.max_temperature) ? prev : current
    })

    return (
        <CardWithValue
            title={'Maximum temperature'}
            date={max_temperature_day.date}
            value_type={'Temperature'}
            value={max_temperature_day.max_temperature}
            station={max_temperature_day.station}
        />
    )
}