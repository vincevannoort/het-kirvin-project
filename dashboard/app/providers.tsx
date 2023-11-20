// app/providers.tsx
'use client'

import { NextUIProvider } from '@nextui-org/react'
import { Button } from '@nextui-org/button'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <NextUIProvider>
      {children}
    </NextUIProvider>
  )
}