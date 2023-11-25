import min_temperature from '@/data/min_temperature.json'
import React from "react";
import { Card, CardHeader, CardBody, Divider } from "@nextui-org/react";
import { format } from 'date-fns';

type CardProperties = {
    title: string,
    date: string,
    value_type: string,
    value: number,
    station: string
}

export function CardWithValue({ title, date, value_type, value, station }: CardProperties) {

    const formattedDate = format(new Date(date), 'd MMMM yyyy');

    return (
        <Card className="mb-5">
            <CardHeader className="px-4 flex-col items-start">
                <p className="text-tiny uppercase font-bold">Daily</p>
                <h4 className="font-bold text-large">{title}</h4>
            </CardHeader>
            <Divider />
            <CardBody>
                <p>
                    Date: {formattedDate}<br />
                    {value_type}: {value}<br />
                    Station: {station}
                </p>
            </CardBody>
        </Card>
    )
}