"use client"
import TemperaturePerStation from '@/components/temperature-per-station'
import SunshinePerStation from '@/components/sunshine-per-station'
import { RainPerDay } from '@/components/rain-per-day'
import { CardMaxTemperature } from '@/components/card-max-temperature'
import { CardMinTemperature } from '@/components/card-min-temperature'
import { CardMostSunshine } from '@/components/card-most-sunshine'
import { CSSProperties } from 'react'
import { CardMostRain } from '@/components/card-most-rain'

export default function Home() {
  const sectionStyle: CSSProperties = {
    // offset scrolling with 4rem (height of navbar) + 2.5rem (space above section) to make space for 
    scrollMarginTop: `calc(4rem + 2.5rem)`,
  }
  return (
    <div className="container mx-auto px-4 pt-10">

      {/* temperature section */}
      <div id="temperature" className="flex flex-wrap lg:flex-nowrap space-x-10" style={sectionStyle}>
        <div className="basis-full lg:basis-3/4 mb-6 lg:mb-0">
          <TemperaturePerStation />
        </div>
        <div className="basis-full lg:basis-1/4">
          <CardMaxTemperature />
          <CardMinTemperature />
        </div>
      </div>
      <hr style={{ margin: 50 }} />

      {/* sunshine section */}
      <div id="sunshine" className="flex space-x-10" style={sectionStyle}>
        <div className="basis-full lg:basis-3/4 mb-6 lg:mb-0">
          <SunshinePerStation />
        </div>
        <div className="basis-full lg:basis-1/4">
          <CardMostSunshine />
        </div>
      </div>
      <hr style={{ margin: 50 }} />

      {/* rain section */}
      <div id="rain" className="flex space-x-10" style={sectionStyle}>
        <div className="basis-full lg:basis-3/4 mb-6 lg:mb-0">
          <RainPerDay />
        </div>
        <div className="basis-full lg:basis-1/4">
          <CardMostRain />
        </div>
      </div>
    </div>
  )
}
