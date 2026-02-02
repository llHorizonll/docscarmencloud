/**
 * Main App component for Carmen Chatbot
 */
import { useEffect } from 'react'
import type { InitOptions } from './types'
import { ChatWidget } from './components/ChatWidget'

interface AppProps {
  apiUrl?: string
  position?: InitOptions['position']
  theme?: InitOptions['theme']
}

export function App({ apiUrl, theme = 'auto' }: AppProps) {
  // Apply theme
  useEffect(() => {
    if (theme === 'auto') {
      const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches
      document.documentElement.classList.toggle('carmen-dark', isDark)
    } else {
      document.documentElement.classList.toggle('carmen-dark', theme === 'dark')
    }
  }, [theme])

  return <ChatWidget apiUrl={apiUrl} />
}
