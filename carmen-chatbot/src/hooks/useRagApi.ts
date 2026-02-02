/**
 * Hook for communicating with the RAG API
 */
import { useState, useCallback } from 'react'
import type { RagResponse } from '../types'

const getApiUrl = (): string => {
  if (typeof window !== 'undefined' && (window as any).CARMEN_CHATBOT_CONFIG) {
    return (window as any).CARMEN_CHATBOT_CONFIG.apiUrl || 'http://127.0.0.1:8001/api/v1'
  }
  return 'http://127.0.0.1:8001/api/v1'
}

export function useRagApi(configUrl?: string) {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const apiUrl = configUrl || getApiUrl()

  const checkHealth = useCallback(async (): Promise<boolean> => {
    try {
      const response = await fetch(`${apiUrl}/health`)
      if (response.ok) {
        const data = await response.json()
        return data.status === 'healthy'
      }
      return false
    } catch {
      return false
    }
  }, [apiUrl])

  const query = useCallback(
    async (
      queryText: string,
      onSuccess: (response: RagResponse) => void,
      onError?: (error: string) => void
    ): Promise<void> => {
      if (!queryText.trim()) return

      setIsLoading(true)
      setError(null)

      try {
        const response = await fetch(`${apiUrl}/query`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            query: queryText,
            language: 'th',
            n_results: 5
          })
        })

        if (!response.ok) {
          throw new Error(`API error: ${response.status}`)
        }

        const data: RagResponse = await response.json()
        onSuccess(data)
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Unknown error'
        setError(errorMessage)
        onError?.(errorMessage)
      } finally {
        setIsLoading(false)
      }
    },
    [apiUrl]
  )

  return {
    query,
    checkHealth,
    isLoading,
    error,
    apiUrl
  }
}
