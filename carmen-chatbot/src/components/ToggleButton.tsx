/**
 * Floating toggle button component
 */
interface ToggleButtonProps {
  isOpen: boolean
  onClick: () => void
  messageCount?: number
}

export function ToggleButton({ isOpen, onClick, messageCount = 0 }: ToggleButtonProps) {
  return (
    <button
      type="button"
      className={`carmen-toggle-btn ${isOpen ? 'open' : ''}`}
      onClick={onClick}
      aria-label="Toggle chat"
    >
      {!isOpen ? (
        <>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" />
          </svg>
          <span className="carmen-toggle-text">Chat</span>
          {messageCount > 1 && (
            <span className="carmen-message-count">{messageCount}</span>
          )}
        </>
      ) : (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M18 6L6 18M6 6l12 12" />
        </svg>
      )}
    </button>
  )
}
