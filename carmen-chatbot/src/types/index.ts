/**
 * TypeScript type definitions for Carmen Chatbot
 */

export type CanCannotStatus = 'can' | 'cannot' | 'cannot_with_workaround' | 'unknown'

export type MessageRole = 'user' | 'assistant'

export interface SourceMetadata {
  module: string
  submodule: string
  doc_type: string
  url: string
  distance: number
}

export interface ChatMessage {
  role: MessageRole
  content: string
  canCannot?: CanCannotStatus
  sources?: SourceMetadata[]
  timestamp?: number
}

export interface RagResponse {
  query: string
  answer: string
  can_cannot: CanCannotStatus
  sources: SourceMetadata[]
  language: string
  processing_time_ms: number
}

export interface RagError {
  error: string
}

export interface InitOptions {
  apiUrl?: string
  position?: 'bottom-right' | 'bottom-left' | 'top-right' | 'top-left'
  theme?: 'auto' | 'light' | 'dark'
}

export interface ChatbotConfig {
  apiUrl: string
  position: string
  theme: string
}
