# StockTrader

A Vue.js application for backtesting stock trading strategies.

## Prerequisites

- Node.js 20 or higher
- pnpm package manager
- Python 3.10 or higher (for the backend API)

## Frontend Setup

1. **Install pnpm** (if not already installed):

   ```sh
   npm install -g pnpm
   ```

2. **Install the necessary dependencies for the frontend**:

   ```sh
   pnpm install
   ```

3. **Run the development server**:
   ```sh
   pnpm dev
   ```

## Backend Setup

1. **Navigate to the backend directory**:

   ```sh
   cd backend
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required Python packages**:

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the backend server**:
   ```sh
   python backend/server.py
   ```

## Running the Application

1. **Start the frontend development server**:

   ```sh
   pnpm dev
   ```

2. **Ensure the backend server is running**:

   ```sh
   python backend/server.py
   ```

3. **Open your browser and navigate to**:
   ```
   http://localhost:3000
   ```

Now you should be able to use the StockTrader application for backtesting stock trading strategies.
