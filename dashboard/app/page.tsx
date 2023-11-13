"use client"
import TemperaturePerStation from '@/components/temperature-per-station'
import SunshinePerStation from '@/components/sunshine-per-station'
import { RainPerDay } from '@/components/rain-per-day'
import CardMaxTemperature from '@/components/card-max-temperature'

export default function Home() {
  return (
    <div className="container mx-auto">
      <div className="flex space-x-10">
        <div className="basis-3/4">
          <TemperaturePerStation />
        </div>
        <div className="basis-1/4">
          <CardMaxTemperature />
        </div>
      </div>
      <hr style={{ margin: 50 }} />
      <SunshinePerStation />
      <hr style={{ margin: 50 }} />
      <RainPerDay />
    </div>
  )
}
