const API_URL = 'http://localhost:5000/api';

const api = {
    async login(username, password) {
        const response = await fetch(`${API_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('token', data.token);
            return true;
        }
        alert(data.message || 'Login failed');
        return false;
    },
    
    logout() {
        localStorage.removeItem('token');
        window.location.href = 'login.html';
    },

    async fetchWithAuth(url, options = {}) {
        const token = localStorage.getItem('token');
        if (!token) {
            window.location.href = 'login.html';
            return;
        }
        
        const headers = {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
            ...(options.headers || {})
        };
        
        const response = await fetch(`${API_URL}${url}`, { ...options, headers });
        if (response.status === 401) {
            this.logout();
        }
        return response;
    }
};
