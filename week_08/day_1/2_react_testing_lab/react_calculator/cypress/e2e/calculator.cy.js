describe("Calculator", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000");
  })

  it('should have working number buttons', () => {
    cy.get('#number2').click();
    cy.get('.display').should('contain', '2')
  });

  it("should update the display with the result of calculation", () => {
    cy.get("#number3").click(); 
    cy.get("#operator-add").click();
    cy.get("#number4").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "7")
  });

  it("should chain multiple operations together", () => {
    cy.get("#number3").click(); 
    cy.get("#operator-add").click();
    cy.get("#number1").click();
    cy.get("#operator-subtract").click();
    cy.get("#number2").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "2")
  });
 
  it("should display a positive number", () => {
    cy.get("#number3").click(); 
    cy.get("#operator-add").click();
    cy.get("#number2").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "5")
  });

  it("should display a negative number", () => {
    cy.get("#number4").click(); 
    cy.get("#operator-subtract").click();
    cy.get("#number8").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "-4")
  });
  
  it("should display a decimal number", () => {
    cy.get("#number5").click(); 
    cy.get("#operator-divide").click();
    cy.get("#number2").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "2.5")
  });

  it("should display very large number to the power of", () => {
    cy.get("#number1").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#number0").click(); 
    cy.get("#operator-multiply").click();
    cy.get("#number1").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#number0").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "1e+24")
  });

  it("should display cannot divide by 0 when divided by 0", () => {
    cy.get("#number5").click(); 
    cy.get("#operator-divide").click();
    cy.get("#number0").click();
    cy.get("#operator-equals").click();
    cy.get(".display").should("contain", "cannot divide by 0")
  });
});