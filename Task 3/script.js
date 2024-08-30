const display = document.getElementById("display");
const buttons = document.querySelectorAll(".number, .operator, .equal, .function");

let currentInput = "";
let previousInput = "";
let operator = "";
let isResultDisplayed = false; // Flag to check if the result is already displayed

buttons.forEach(button => {
    button.addEventListener("click", () => {
        if (button.classList.contains("number")) {
            if (isResultDisplayed) {
                // Reset for a new calculation if result was displayed
                currentInput = button.value;
                isResultDisplayed = false;
            } else {
                currentInput += button.value;
            }
            display.value = currentInput;
        } else if (button.classList.contains("operator")) {
            if (previousInput !== "" && operator !== "") {
                calculate();
            }
            operator = button.value;
            previousInput = currentInput;
            currentInput = "";
            display.value = operator; // Show only the operator for the next input
            isResultDisplayed = false;
        } else if (button.classList.contains("equal")) {
            calculate();
        } else if (button.classList.contains("function")) {
            handleFunction(button.value);
        }
    });
});

function calculate() {
    if (previousInput === "" || currentInput === "" || operator === "") {
        return; // Prevent calculation if not all inputs are present
    }

    let result;
    switch (operator) {
        case "+":
            result = parseFloat(previousInput) + parseFloat(currentInput);
            break;
        case "-":
            result = parseFloat(previousInput) - parseFloat(currentInput);
            break;
        case "*":
            result = parseFloat(previousInput) * parseFloat(currentInput);
            break;
        case "/":
            result = parseFloat(previousInput) / parseFloat(currentInput);
            break;
        default:
            return;
    }
    display.value = result; // Show only the result
    currentInput = result.toString();
    previousInput = "";
    operator = "";
    isResultDisplayed = true; // Set flag to true after displaying result
}

function handleFunction(func) {
    if (func === "C") {
        currentInput = "";
        previousInput = "";
        operator = "";
        display.value = "";
        isResultDisplayed = false;
    } else if (func === "CE") {
        currentInput = "";
        display.value = currentInput;
        isResultDisplayed = false;
    } else if (func === "backspace") {
        currentInput = currentInput.slice(0, -1);
        display.value = currentInput;
        isResultDisplayed = false;
    } else if (func === "%") {
        currentInput = (parseFloat(currentInput) / 100).toString();
        display.value = currentInput;
        isResultDisplayed = false;
    }
}
