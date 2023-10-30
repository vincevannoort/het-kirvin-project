"use client"
import Chart from '@/components/chart'
import styles from './page.module.css'

export default function Home() {
  return (
    <main className={styles.container}>
      <Chart />
    </main>
  )
}
