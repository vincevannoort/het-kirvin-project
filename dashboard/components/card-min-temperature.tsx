import min_temperature from '@/data/min_temperature.json'
import React from "react";
import { CardWithValue } from './card-with-value';




export default function CardMinTemperature() {

    const min_temperature_day = min_temperature.reduce(function (prev, current) {
        return (prev && prev.min_temperature < current.min_temperature) ? prev : current
    })

    return (
        <CardWithValue
            title={'Minimum temperature'}
            date={min_temperature_day.date}
            value_type={'Temperature'}
            value={min_temperature_day.min_temperature}
            station={min_temperature_day.station}
        />
    )
}