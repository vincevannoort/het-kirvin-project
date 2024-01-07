"use client"

import Datepicker, { DateValueType } from "react-tailwindcss-datepicker";

import { create } from 'zustand'

type DateRange = {
    startDate: Date,
    endDate: Date,
}

interface DateRangeState {
    dateRange: DateRange
    update: (value: DateValueType) => void
}

export function timestamp_within_date_range(timestamp: number, dateRange: DateRange): boolean {
    return timestamp >= dateRange.startDate.getTime() && timestamp <= dateRange.endDate.getTime()
}

export const useDateRangeStore = create<DateRangeState>()((set) => ({
    dateRange: {
        // set start date to one year ago
        startDate: (() => {
            let startDate = new Date()
            startDate.setFullYear(new Date().getFullYear() - 1)
            return startDate
        })(),
        endDate: new Date(),
    },
    // handles updates from the date range picker to the data store
    // 
    // the `DateValueType` is type provided by react-tailwindcss-datepicker, 
    // which we receive as updates from the `Datepicker` component,
    // this update function then only updates the `dateRange` state when
    // the `DateValueType` contains a `startDate` and `endDate`
    update: (value: DateValueType) => {
        // do not update when `startDate` or `endDate` is missing
        if (!value || !value.startDate || !value.endDate) {
            return
        }

        set({
            dateRange: {
                startDate: new Date(value.startDate),
                endDate: new Date(value.endDate),
            }
        })
    },
}))


export function DateRangePicker() {
    const { update, dateRange } = useDateRangeStore();

    return (
        <>
            <div className="flex items-center py-4">
                <p className="whitespace-nowrap">Date range:</p>
                <Datepicker
                    value={dateRange}
                    onChange={update}
                    showShortcuts={true}
                    containerClassName={"relative text-gray-700"}
                />
            </div>
        </>
    );
}