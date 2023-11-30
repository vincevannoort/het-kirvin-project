"use client"
import TemperaturePerStation from '@/components/temperature-per-station'
import SunshinePerStation from '@/components/sunshine-per-station'
import { RainPerDay } from '@/components/rain-per-day'
import { CardMaxTemperature } from '@/components/card-max-temperature'
import { CardMinTemperature } from '@/components/card-min-temperature'
import { CardMostSunshine } from '@/components/card-most-sunshine'
import { CSSProperties } from 'react'
import { CardMostRain } from '@/components/card-most-rain'
import { CardDayStatistics } from '@/components/card-day-statistics'

type SectionProperties = {
  id: string,
  left: JSX.Element,
  right: JSX.Element,
}


function Section({ id, left, right }: SectionProperties) {
  const sectionStyle: CSSProperties = {
    // offset scrolling with 4rem (height of navbar) + 2.5rem (space above section) to make space for 
    scrollMarginTop: `calc(4rem + 2.5rem)`,
  }
  return (
    <div id={id} className="flex flex-wrap lg:flex-nowrap lg:space-x-10" style={sectionStyle}>
      <div className="basis-full lg:basis-3/4 mb-6 lg:mb-0">
        {left}
      </div>
      <div className="basis-full lg:basis-1/4">
        {right}
      </div>
    </div>
  )
}

export default function Home() {
  return (
    <div className="container mx-auto px-4 pt-4 pb-8 md:py-16">

      {/* temperature section */}
      <Section
        id="temperature"
        left={
          <TemperaturePerStation />
        }
        right={(
          <>
            <CardMaxTemperature />
            <CardMinTemperature />
          </>
        )}
      />
      <hr className='my-4 md:my-12' />

      {/* sunshine section */}
      <Section
        id="sunshine"
        left={
          <SunshinePerStation />
        }
        right={
          <CardMostSunshine />
        }
      />
      <hr className='my-4 md:my-12' />

      {/* rain section */}
      <Section
        id="rain"
        left={
          <RainPerDay />
        }
        right={
          <CardMostRain />
        }
      />

      <CardDayStatistics />
    </div>
  )
}
