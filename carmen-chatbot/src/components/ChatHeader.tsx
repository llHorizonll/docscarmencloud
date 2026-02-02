/**
 * Chat header component
 */
interface ChatHeaderProps {
  isMinimized: boolean
  onMinimize: () => void
  onClear: () => void
  isHealthy: boolean
}

export function ChatHeader({
  isMinimized,
  onMinimize,
  onClear,
  isHealthy
}: ChatHeaderProps) {
  const handleClose = () => {
    // Call close if CarmenChatbot exists and has close method
    if (typeof window !== 'undefined' && window.CarmenChatbot) {
      const widget = window.CarmenChatbot()
      widget?.close?.()
    }
  }

  return (
    <div className="carmen-chat-header">
      <div className="carmen-header-left">
        <h3>Carmen AI</h3>
        <div className={`carmen-health-dot ${isHealthy ? 'healthy' : 'unhealthy'}`} />
      </div>
      <div className="carmen-header-right">
        <button
          type="button"
          className="carmen-icon-button"
          onClick={onClear}
          title="Clear chat"
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2" />
          </svg>
        </button>
        <button
          type="button"
          className="carmen-icon-button"
          onClick={onMinimize}
          title={isMinimized ? 'Expand' : 'Minimize'}
        >
          {isMinimized ? (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" />
            </svg>
          ) : (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M8 3v3a2 2 0 01-2 2H3m18 0h-3a2 2 0 01-2-2V3m0 18v-3a2 2 0 012-2h3M3 16h3a2 2 0 012 2v3" />
            </svg>
          )}
        </button>
        <button
          type="button"
          className="carmen-icon-button"
          onClick={handleClose}
          title="Close"
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M18 6L6 18M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>
  )
}
