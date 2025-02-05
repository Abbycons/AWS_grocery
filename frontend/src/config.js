// Get the runtime config from window object or use environment variables
const getRuntimeConfig = () => {
    // Check if we have runtime config injected and it's not the template string
    if (window.__RUNTIME_CONFIG__ && 
        window.__RUNTIME_CONFIG__.BACKEND_URL && 
        window.__RUNTIME_CONFIG__.BACKEND_URL !== "{{BACKEND_URL}}") {
        return {
            BACKEND_URL: window.__RUNTIME_CONFIG__.BACKEND_URL
        };
    }
    
    // Fallback to default
    return {
        BACKEND_URL: 'http://localhost:8081'
    };
};

export const config = getRuntimeConfig(); 