import React from "react";
import { Card, CardHeader, CardBody, Divider, Select, SelectItem } from "@nextui-org/react";
import most_rainfall from '@/data/most_rainfall.json'

export function CardDayStatistics() {

    //let rain_value = most_rainfall.reduce

    return (
        <Card className="mb-5">
            <CardHeader className="px-4 flex-col items-start">
                <h4 className="font-bold uppercase text-large">{'Inspect'}</h4>
                <Select
                    label="Select a day"
                    className="max-w-xs"
                >
                </Select>
                <Select
                    label="Select a station"
                    className="max-w-xs"
                >
                </Select>
            </CardHeader>
            <Divider />
            <CardBody>
                <p>
                    Average temperature: 20 degrees<br />
                    Sunshine duration: 2.5 hours<br />
                    Rain amount: 3 mm<br />
                </p>
            </CardBody>
        </Card>
    )
}