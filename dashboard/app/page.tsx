"use client"
import styles from './page.module.css'
import TemperaturePerStation from '@/components/temperature-per-station'

export default function Home() {
  return (
    <div className={styles.container}>
      <TemperaturePerStation />
    </div>
  )
}
