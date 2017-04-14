Feature: Elementos

    As common user
    I want to see all neighborhoods
    And all categories

    Scenario: See all neighborhoods

        When I request to see all neighborhood
        Then I will see all available neighborhoods

    Scenario: See all categories

        When I request to see all categories
        Then I will see all available categories

    Scenario: See all elements from a neighborhoods

        When I request to see all elements from a certain neighborhood
        Then I will see all available elements in that neighborhood

    Scenario: See all elements from a category

        When I request to see all elements from a certain category
        Then I will see all available elements in that category

    Scenario: See all elements from a neighborhood and category

        When I request to see all elements from a neighborhood and category
        Then I will see all available elements in that neighborhood and category


    Scenario: See a specific information about an element

        When I request to see all information about an element
        Then I will be able to see that information
