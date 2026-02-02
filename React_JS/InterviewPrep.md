**Structure:**

1. **What it is**
2. **How it works**
3. **Example / mental model (only if it adds value)**

Think: *“Explain it to a 5-year-old, but the 5-year-old is a junior dev.”*

---

# 1. What is React?

### What it is

React is a **JavaScript library** used to build **user interfaces**, mainly for web applications.
It focuses **only on the UI layer**, not routing, not data fetching, not state management libraries — just UI.

### How it works

React lets us:

* Break UI into **components**
* Describe UI using **JSX**
* Control UI using **state and props**
  When state or props change, React **re-renders** the affected parts of the UI.

### Mental model

React is like a **UI machine**:

> “Here is my data → now show me the UI for this data.”

---

# 2. What are Components?

### What it is

Components are **JavaScript functions (previously also classes)** that:

* Return **JSX**
* Represent a **piece of UI**
* Can accept **props**
* Can manage **state**

### How it works

React calls these functions to get JSX.
That JSX is later converted into real DOM elements.

### Example / mental model

A component is like a **mold**:

* Same logic
* Different data
* Same UI structure

---

# 3. Functional vs Class Components

### What it is

Two ways to define components:

* **Functional components** → plain JS functions
* **Class components** → ES6 classes (mostly legacy)

### How it works

* Functional components use **hooks** (`useState`, `useEffect`)
* Class components use `this.state`, `setState`, lifecycle methods

### Key point

Today:

> **Functional components + hooks = standard React**

---

# 4. What is JSX?

### What it is

JSX is **syntax sugar** that lets us write HTML-like code inside JavaScript.

### How it works

JSX is **not HTML**.
It gets compiled into:

```js
React.createElement()
```

### Mental model

JSX is just a **friendlier way** to write React elements.

---

# 5. Props

### What it is

Props are **inputs** passed to a component from its parent.

### How it works

* Props flow **top → down**
* Props are **read-only**
* Child cannot modify props

### Mental model

Props are like **function arguments** for components.

---

# 6. State

### What it is

State is **data owned by a component** that can change over time.

### How it works

* State changes trigger **re-renders**
* State is managed using hooks (`useState`) in functional components

### Mental model

State is what makes UI **dynamic**.

---

# 7. Props vs State

### What it is

Two ways of handling data in React.

### How it works

* Props → external, read-only
* State → internal, mutable

### Golden line

> Props configure a component.
> State controls a component.

---

# 8. What are Hooks?

### What it is

Hooks are **JavaScript functions provided by React** that let functional components use React features.

### How it works

Hooks let us:

* Store state
* Run side effects
* Access context
  without using class components.

### Rule (important)

Hooks:

* Only called at top level
* Only inside React functions

---

# 9. useState (your style, tightened)

### What it is

`useState` is a **hook** that allows a **functional component** to have and control state.

### How it works

* `useState` is a **JavaScript function**
* It takes an **initial value**
* It returns an **array with two items**

1. Current state value
2. State setter function

Calling the setter:

* Updates the state
* Triggers a re-render

### Mental model

State = memory of a component.

---

# 10. useEffect

### What it is

`useEffect` is a hook used to perform **side effects** in a component.

### How it works

React runs `useEffect` **after rendering**.
Side effects include:

* API calls
* Timers
* Subscriptions
* Manual DOM operations

### Mental model

Render first → then do extra work.

---

# 11. Dependency Array in useEffect

### What it is

The dependency array controls **when the effect runs**.

### How it works

* `[]` → runs once (on mount)
* `[x]` → runs when `x` changes
* No array → runs on every render

Cleanup function runs before next effect or unmount.

---

# 12. Virtual DOM

### What it is

The virtual DOM is a **JavaScript representation** of the real DOM.

### How it works

* React updates virtual DOM first
* Compares old vs new (diffing)
* Updates only changed parts in real DOM

### Mental model

React doesn’t repaint the whole wall, only the cracked tiles.

---

# 13. React Rendering Process

### What it is

Rendering is React turning components into UI.

### How it works

1. State/props change
2. Component function runs again
3. New virtual DOM created
4. Differences calculated
5. Real DOM updated minimally

---

# 14. Conditional Rendering

### What it is

Rendering UI **based on conditions**.

### How it works

Uses:

* `if`
* ternary operator
* `&&`

### Mental model

Same component, different UI states.

---

# 15. Event Handling in React

### What it is

Handling user actions like click, submit, change.

### How it works

* Uses camelCase (`onClick`)
* Passes functions, not strings
* Uses synthetic events

---

# 16. Parent to Child Data Flow

### What it is

Passing data from parent component to child.

### How it works

Using **props**.

### Mental model

Parent owns data, child consumes it.

---

# 17. Lifting State Up

### What it is

Moving shared state to a common parent.

### How it works

* Parent stores state
* Passes state + setters to children

### Golden point

Single source of truth.

---

# 18. Controlled vs Uncontrolled Components

### What it is

Two ways to handle form inputs.

### How it works

* Controlled → React controls value
* Uncontrolled → DOM controls value via ref

### Interview truth

Controlled components are preferred.

---

# 19. Forms in React

### What it is

Forms handled using controlled inputs.

### How it works

* Input value bound to state
* Changes handled via `onChange`
* Submission via `onSubmit`

---

# 20. Keys in Lists

### What it is

Keys uniquely identify list items.

### How it works

Keys help React:

* Track items
* Optimize re-renders
* Avoid UI bugs

### Rule

Never use index unless no other option.

---

# 21. map vs forEach in React

### What it is

Two array methods.

### How it works

* `map` returns a new array → required for JSX
* `forEach` returns nothing → useless for rendering

---

# 22. Fetching Data in React

### What it is

Getting data from external APIs.

### How it works

* Usually done in `useEffect`
* On component mount
* Update state with response

### Mental model

Fetch → store in state → render UI.

---

# 23. What is `useContext`?

### What it is

`useContext` is a **hook** that allows a component to **consume data from React Context** without passing props manually at every level.

### How it works

* Context is created using `createContext`
* A **Provider** wraps components and supplies a value
* Any child component can access that value using `useContext`

This avoids unnecessary prop passing.

### Mental model

Instead of handing notes through every student in the class, you **announce it once** and everyone can hear it.

---

# 24. What is prop drilling and how do you avoid it?

### What it is

Prop drilling is when you pass props through **multiple components** just to reach a deeply nested child.

### How it works

* Parent has data
* Intermediate components don’t need it
* But still must pass it down

This makes code **messy and hard to maintain**.

### How to avoid it

* React Context
* State management libraries (Redux, Zustand)

### Mental model

Passing a message through 5 people when only the last person needs it.

---

# 25. What is `useRef`?

### What it is

`useRef` is a hook that provides a **mutable object** which persists across renders **without causing re-renders**.

### How it works

* `useRef` returns an object with a `.current` property
* Updating `.current` does **not** re-render the component
* Commonly used to:

  * Access DOM elements
  * Store values between renders

### Mental model

A **box** that React ignores during re-rendering.

---

# 26. What are Fragments?

### What it is

Fragments let you group multiple JSX elements **without adding extra DOM nodes**.

### How it works

Instead of wrapping with a `<div>`, you use:

```jsx
<>
  <h1 />
  <p />
</>
```

### Mental model

An **invisible wrapper**.

---

# 27. What is reconciliation?

### What it is

Reconciliation is the process React uses to **compare old and new virtual DOM trees**.

### How it works

* React re-renders components
* Creates a new virtual DOM
* Compares it with the previous one
* Finds minimal changes
* Updates real DOM accordingly

### Mental model

Spot-the-difference between two UI snapshots.

---

# 28. What is lazy loading?

### What it is

Lazy loading is a technique where components are **loaded only when needed**.

### How it works

* Uses `React.lazy`
* Loads components dynamically
* Reduces initial bundle size

### Mental model

You don’t load the whole book — you open the page when you reach it.

---

# 29. What is code splitting?

### What it is

Code splitting is breaking your JavaScript bundle into **smaller chunks**.

### How it works

* Done using dynamic imports
* Lazy loading is one form of code splitting
* Improves performance and load time

### Mental model

Instead of one heavy bag, you carry **multiple light bags**.


