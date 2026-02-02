/**
 * localStorage hook for chatbot state persistence
 */
import { useState } from 'react'

const STORAGE_KEY = 'carmen-chatbot-history'

export function useLocalStorage<T>(key: string, initialValue: T) {
  // Initialize state with function to read from localStorage synchronously
  const [storedValue, setStoredValue] = useState<T>(() => {
    if (typeof window === 'undefined') return initialValue
    try {
      const item = window.localStorage.getItem(key)
      if (item) {
        const parsed = JSON.parse(item)
        // Use stored value if valid
        if (parsed && (Array.isArray(parsed) ? parsed.length > 0 : parsed)) {
          console.log('[useLocalStorage] Loaded from storage:', parsed)
          return parsed
        }
      }
    } catch (error) {
      console.error(`Error loading ${key} from localStorage:`, error)
    }
    console.log('[useLocalStorage] Using initial value:', initialValue)
    return initialValue
  })

  // Save to localStorage whenever value changes
  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value
      setStoredValue(valueToStore)
      if (typeof window !== 'undefined') {
        window.localStorage.setItem(key, JSON.stringify(valueToStore))
        console.log('[useLocalStorage] Saved to storage:', valueToStore)
      }
    } catch (error) {
      console.error(`Error saving ${key} to localStorage:`, error)
    }
  }

  const clearValue = () => {
    try {
      setStoredValue(initialValue)
      if (typeof window !== 'undefined') {
        window.localStorage.removeItem(key)
      }
    } catch (error) {
      console.error(`Error clearing ${key} from localStorage:`, error)
    }
  }

  return [storedValue, setValue, clearValue] as const
}

export { STORAGE_KEY }
