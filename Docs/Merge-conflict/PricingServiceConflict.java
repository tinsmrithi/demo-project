This file shows the merge conflict that appears in PricingService.java when
you pull main after implementing the new rule engine on your feature branch.

Your branch rewrote applyDiscount() to use the new PricingRuleEngine.
A colleague on main added a null guard for customer == null in the same method.

The conflict looks like this:

        <<<<<<< HEAD (your branch: feature/b2b-pricing)
public BigDecimal applyDiscount(Customer customer, BigDecimal orderTotal) {
    PricingRule rule = ruleEngine.getRuleForCustomer(customer);
    return rule.apply(orderTotal);
}
=======
public BigDecimal applyDiscount(Customer customer, BigDecimal orderTotal) {
    if (customer == null) return orderTotal;
    return orderTotal.multiply(BigDecimal.valueOf(0.9));
}
>>>>>>> main

Both changes are intentional and correct:
        - Your branch: introduces the rule engine for configurable B2B pricing
- Main: adds a null guard that prevents NPE when customer is not loaded

The correct merged result preserves both:
public BigDecimal applyDiscount(Customer customer, BigDecimal orderTotal) {
    if (customer == null) return orderTotal;
    PricingRule rule = ruleEngine.getRuleForCustomer(customer);
    return rule.apply(orderTotal);
}