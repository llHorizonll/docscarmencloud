/**
 * Health status indicator component
 */
interface HealthIndicatorProps {
  isHealthy: boolean
}

export function HealthIndicator({ isHealthy }: HealthIndicatorProps) {
  return (
    <div
      className={`carmen-health-indicator ${isHealthy ? 'healthy' : 'unhealthy'}`}
      title={isHealthy ? 'API Connected' : 'API Disconnected'}
    />
  )
}
