import most_sunshine from '@/data/most_sunshine.json'
import React from "react";
import { CardWithValue } from './card-with-value';


export default function CardMostSunshine() {

    const most_sunshine_day = most_sunshine.reduce(function (prev, current) {
        return (prev && prev.max_sunshine_duration > current.max_sunshine_duration) ? prev : current
    })

    return (
        <CardWithValue
            title={'Most sunshine'}
            date={most_sunshine_day.date}
            value_type={'Sunshine hours'}
            value={most_sunshine_day.max_sunshine_duration}
            station={most_sunshine_day.station ? most_sunshine_day.station : 'unknown'}
        />
    )
}