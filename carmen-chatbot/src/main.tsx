/**
 * Entry point for Carmen Chatbot
 * Initializes the widget and exposes it globally
 */
import React from 'react'
import ReactDOM from 'react-dom/client'
import { App } from './App'
import type { InitOptions } from './types'
import './styles/index.css'

// Global widget instance
let currentRoot: ReactDOM.Root | null = null
let rootElement: HTMLElement | null = null

// Type for widget control object
type WidgetControl = {
  destroy: () => void
  close: () => void
}

// Type for the init function
type InitCarmenChatbot = (options?: InitOptions) => WidgetControl

// Extend Window interface
declare global {
  interface Window {
    CarmenChatbot?: InitCarmenChatbot
    CARMEN_CHATBOT_CONFIG?: InitOptions
  }
}

/**
 * Initialize the Carmen Chatbot widget
 * @param options - Configuration options
 * @returns Widget control object
 */
const initCarmenChatbot: InitCarmenChatbot = (options = {}) => {
  const {
    apiUrl = 'http://127.0.0.1:8001/api/v1',
    position = 'bottom-right',
    theme = 'auto'
  } = options

  // Remove existing instance if any
  destroyCarmenChatbot()

  // Create root element
  rootElement = document.createElement('div')
  rootElement.id = 'carmen-chatbot-root'
  document.body.appendChild(rootElement)

  // Apply position
  rootElement.className = `carmen-chatbot-wrapper position-${position}`

  // Mount React app
  currentRoot = ReactDOM.createRoot(rootElement)
  currentRoot.render(
    <React.StrictMode>
      <App apiUrl={apiUrl} position={position} theme={theme} />
    </React.StrictMode>
  )

  return {
    destroy: destroyCarmenChatbot,
    close: () => {
      const widget = rootElement?.querySelector('.carmen-chatbot-container')
      if (widget) {
        widget.classList.remove('open')
      }
    }
  }
}

/**
 * Destroy the chatbot widget
 */
function destroyCarmenChatbot() {
  if (currentRoot) {
    currentRoot.unmount()
    currentRoot = null
  }
  if (rootElement) {
    rootElement.remove()
    rootElement = null
  }
}

// Expose globally for script tag usage
window.CarmenChatbot = initCarmenChatbot

// Auto-init if config is present
if (typeof window !== 'undefined' && window.CARMEN_CHATBOT_CONFIG) {
  initCarmenChatbot(window.CARMEN_CHATBOT_CONFIG)
}

export default initCarmenChatbot
export { destroyCarmenChatbot }
