// Get the backend URL from the current window location
const getRuntimeConfig = () => {
    // Get the current window location
    const location = window.location;
    const hostname = location.hostname;
    
    // Always use port 8080 for localhost
    const port = '8080';
    
    // Construct the backend URL
    const origin = `http://${hostname}:${port}`;
    
    // Log the configuration for debugging
    console.log('Window location:', location);
    console.log('Using hostname:', hostname);
    console.log('Using port:', port);
    console.log('Using backend URL:', origin);
    
    return {
        BACKEND_URL: `${origin}/api`  // Add /api prefix to all requests
    };
};

const config = getRuntimeConfig();

// Log the final configuration
console.log('Final config:', config);

export { config }; 