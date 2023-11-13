"use client"

import max_temperature from '@/data/max_temperature.json'
import Highcharts, { SeriesLineOptions, SeriesOptionsType } from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import React from "react";
import { Card, CardHeader, CardBody, CardFooter, Divider, Link, Image } from "@nextui-org/react";




export default function CardMaxTemperature() {

    const max_temperature_day = max_temperature.reduce(function (prev, current) {
        return (prev && prev.max_temperature > current.max_temperature) ? prev : current
    })

    return (
        <Card className="h-full">
            <CardHeader className="px-4 flex-col items-start">
                <p className="text-tiny uppercase font-bold">Daily Mix</p>
                <h4 className="font-bold text-large">Maximum temperature</h4>
            </CardHeader>
            <Divider />
            <CardBody>
                <p>
                    Date: {max_temperature_day.date}<br />
                    Temperature: {max_temperature_day.max_temperature}<br />
                    Station: {max_temperature_day.station}
                </p>
            </CardBody>
        </Card>
    )
}