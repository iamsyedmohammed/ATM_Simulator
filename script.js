document.getElementById('atm-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const deposit = parseFloat(document.getElementById('deposit').value);
  const mode = document.getElementById('mode').value;
  const withdraw = parseFloat(document.getElementById('withdraw').value);
  const password = document.getElementById('password').value;
  const messageEl = document.getElementById('message');

  const messages = [];

  if (isNaN(deposit) || deposit <= 0) {
    messages.push('Enter a valid deposit amount.');
  }

  if (mode === 'Cr') {
    messages.push('You have used Credit transaction with a limit of 30000.');
  } else if (mode === 'Dr') {
    messages.push('You have chosen Debit.');
  } else {
    messages.push('Invalid mode of transaction.');
  }

  if (isNaN(withdraw) || withdraw <= 0) {
    messages.push('Enter a valid withdraw amount.');
  } else if (withdraw > deposit) {
    messages.push("You don't have sufficient funds.");
  }

  if (password !== 'xyz@123') {
    messages.push('Invalid password.');
  }

  if (messages.length === 0) {
    const newBalance = deposit - withdraw;
    messages.push('Your transaction was successful.');
    messages.push(`Total amount left is ₹${newBalance}`);
  }

  messageEl.innerHTML = messages.map((m) => `<p>${m}</p>`).join('');
});
