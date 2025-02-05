// Get the backend URL from environment variables or window location
const getRuntimeConfig = () => {
    // Get the current window location
    const location = window.location;
    
    // Get host and port from environment variables or defaults
    const host = process.env.REACT_APP_BACKEND_HOST || location.hostname || 'localhost';
    const port = process.env.REACT_APP_BACKEND_PORT || location.port || '8080';
    
    // Construct the backend URL
    const origin = `http://${host}:${port}`;
    
    // Log the configuration for debugging
    console.log('Configuration:', {
        location,
        host,
        port,
        origin
    });
    
    return {
        BACKEND_URL: `${origin}/api`  // Add /api prefix to all requests
    };
};

const config = getRuntimeConfig();

// Log the final configuration
console.log('Final config:', config);

export { config }; 