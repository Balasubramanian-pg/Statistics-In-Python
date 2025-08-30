Of course. This is a fantastic topic to review, as these two rules are the absolute bedrock of calculating probabilities for combined events.

The easiest way to remember which rule to use is by associating them with keywords:
*   **Addition Rule** is for **"OR"** events: What is the probability of event A *or* event B happening?
*   **Multiplication Rule** is for **"AND"** events: What is the probability of event A *and then* event B happening?

Let's break them down.

---

### 1. The Addition Rule (For "OR" Events)

The Addition Rule helps us find the probability that *at least one* of two events will occur. The key is to know whether the events can happen at the same time or not.

#### a) For Mutually Exclusive Events

**Definition:** Two events are **mutually exclusive** if they **cannot happen at the same time**.
*   **Example:** In a single roll of a die, you cannot roll both a 2 and a 5. These events are mutually exclusive.

**The Rule:** If events A and B are mutually exclusive, the probability of A or B occurring is simply the sum of their individual probabilities.

**Formula: P(A or B) = P(A) + P(B)**

**Example: Rolling a Die**
*   **Question:** What is the probability of rolling a 2 or a 5?
*   **P(2):** 1/6
*   **P(5):** 1/6
*   **P(2 or 5) = P(2) + P(5) = 1/6 + 1/6 = 2/6 = 1/3**

#### b) For Non-Mutually Exclusive Events

**Definition:** Two events are **non-mutually exclusive** if they **can happen at the same time**.
*   **Example:** When drawing one card from a deck, you can draw a card that is both a King and a Heart (the King of Hearts). These events are non-mutually exclusive.

**The Rule:** If events A and B are non-mutually exclusive, we add their probabilities but then **subtract the probability of their overlap** to avoid double-counting.

**Formula: P(A or B) = P(A) + P(B) - P(A and B)**

**Example: Drawing a Card**
*   **Question:** What is the probability of drawing a King or a Heart?
*   **P(King):** There are 4 Kings in a 52-card deck, so P(King) = 4/52.
*   **P(Heart):** There are 13 Hearts in a 52-card deck, so P(Heart) = 13/52.
*   **P(King and Heart):** There is one card that is both, the King of Hearts. So, P(King and Heart) = 1/52.
*   **P(King or Heart) = P(King) + P(Heart) - P(King and Heart)**
    = 4/52 + 13/52 - 1/52
    = 16/52 = 4/13

---

### 2. The Multiplication Rule (For "AND" Events)

The Multiplication Rule helps us find the probability that two (or more) events will occur in sequence. The key here is to know if the events are independent or dependent.

#### a) For Independent Events

**Definition:** Two events are **independent** if the outcome of the first event **does not affect** the probability of the second event.
*   **Example:** Flipping a coin twice. The result of the first flip has no impact on the second flip.

**The Rule:** If events A and B are independent, the probability of both A and B occurring is the product of their individual probabilities.

**Formula: P(A and B) = P(A) × P(B)**

**Example: Flipping a Coin Twice**
*   **Question:** What is the probability of getting Heads on the first flip AND Heads on the second flip?
*   **P(Heads on 1st flip):** 1/2
*   **P(Heads on 2nd flip):** 1/2
*   **P(Heads and Heads) = P(H1) × P(H2) = 1/2 × 1/2 = 1/4**

#### b) For Dependent Events

**Definition:** Two events are **dependent** if the outcome of the first event **changes** the probability of the second event.
*   **Example:** Drawing two cards from a deck *without replacement*. After you draw the first card, there are fewer cards left, which changes the probabilities for the second draw.

**The Rule:** If events A and B are dependent, the probability of both A and B occurring is the probability of A multiplied by the **conditional probability** of B occurring, given that A has already occurred.

**Formula: P(A and B) = P(A) × P(B|A)**
*   `P(B|A)` reads "the probability of B, given A."

**Example: Drawing Two Cards (Without Replacement)**
*   **Question:** What is the probability of drawing a King first AND a Queen second?
*   **P(King on 1st draw):** 4/52
*   **P(Queen on 2nd draw | King on 1st draw):** After drawing a King, there are now only 51 cards left in the deck. The 4 Queens are all still there. So, the probability of drawing a Queen next is 4/51.
*   **P(King and Queen) = P(K1) × P(Q2|K1)**
    = (4/52) × (4/51)
    = 16 / 2652 ≈ 0.006

### Summary Table

| You Want to Find... | And the Events are... | Rule to Use | Formula |
| :--- | :--- | :--- | :--- |
| **P(A or B)** | **Mutually Exclusive** (can't happen together) | Simple Addition Rule | `P(A) + P(B)` |
| **P(A or B)** | **Non-Mutually Exclusive** (can happen together) | General Addition Rule | `P(A) + P(B) - P(A and B)` |
| **P(A and B)** | **Independent** (outcome of A doesn't affect B) | Simple Multiplication Rule | `P(A) × P(B)` |
| **P(A and B)** | **Dependent** (outcome of A affects B) | General Multiplication Rule | `P(A) × P(B|A)` |