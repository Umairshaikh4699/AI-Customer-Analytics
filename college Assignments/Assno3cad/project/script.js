// --- Wallet State ---
// Start with an initial balance (must be a number, not a string with '₹')
let currentBalance = 500.00; 

// References to HTML elements
const balanceDisplay = document.getElementById('balanceDisplay');
const transactionList = document.getElementById('transactionList');
const addMoneyBtn = document.getElementById('addMoneyBtn');
const payNowBtn = document.getElementById('payNowBtn');

// Function to update the balance shown on the screen
function updateBalanceDisplay() {
    // Format the number back into a currency string for display
    balanceDisplay.textContent = `₹ ${currentBalance.toFixed(2)}`;
}

// Function to add a new transaction to the list
function addTransaction(description, amount) {
    const listItem = document.createElement('li');
    let sign = (amount > 0) ? '+' : '-'; // Determine if it's a deposit or withdrawal
    
    // Create the transaction list item text
    listItem.innerHTML = `${description} - **${sign} ₹ ${Math.abs(amount).toFixed(2)}**`;
    
    // Add the new transaction to the top of the list
    transactionList.prepend(listItem);
}

// --- Event Handlers for Buttons ---

// 1. Add Money Handler
addMoneyBtn.addEventListener('click', () => {
    // In a real app, this would trigger a payment gateway.
    // Here, we simulate a deposit of ₹ 100
    const depositAmount = 100.00;
    
    currentBalance += depositAmount; // Update the balance
    
    addTransaction('Wallet Deposit (Simulated)', depositAmount); // Add transaction record
    updateBalanceDisplay(); // Refresh the screen display
    
    alert(`Successfully deposited ₹ ${depositAmount.toFixed(2)}.`);
});

// 2. Pay Now Handler
payNowBtn.addEventListener('click', () => {
    // In a real app, this would prompt for a merchant and amount.
    // Here, we simulate a small purchase (e.g., Canteen)
    
    let purchaseAmount = prompt("Enter amount to pay (e.g., 25.00):");
    
    // Check if the user entered an amount and if it's a valid number
    if (purchaseAmount && !isNaN(purchaseAmount) && parseFloat(purchaseAmount) > 0) {
        purchaseAmount = parseFloat(purchaseAmount);
        
        if (currentBalance >= purchaseAmount) {
            // Valid transaction
            currentBalance -= purchaseAmount; // Update the balance
            
            addTransaction('Canteen Purchase (Simulated)', -purchaseAmount); // Add transaction record (negative for withdrawal)
            updateBalanceDisplay(); // Refresh the screen display
            
            alert(`Payment of ₹ ${purchaseAmount.toFixed(2)} successful!`);
            
        } else {
            // Insufficient funds
            alert("Transaction failed. Insufficient balance.");
        }
    } else if (purchaseAmount !== null) {
        // User clicked OK but entered invalid data
        alert("Invalid amount entered. Please try again.");
    }
    // If user clicked Cancel, do nothing
});

// Initialize the display when the page loads
updateBalanceDisplay();