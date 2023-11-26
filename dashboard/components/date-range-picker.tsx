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
        startDate: new Date(new Date().getFullYear(), 0, 1),
        endDate: new Date(),
    },
    // input is type provided by react-tailwindcss-datepicker, 
    // we convert it to our own type which cannot be null
    update: (value) => {
        // ensure we always have a valid date range
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