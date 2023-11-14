"use client"
import styles from './page.module.css'
import TemperaturePerStation from '@/components/temperature-per-station'
import SunshinePerStation from '@/components/sunshine-per-station'
import { RainPerDay } from '@/components/rain-per-day'

export default function Home() {
  return (
    <div className={styles.container}>
      <TemperaturePerStation />
      <hr style={{ margin: 50 }} />
      <SunshinePerStation />
      <hr style={{ margin: 50 }} />
      <RainPerDay />
    </div>
  )
}
