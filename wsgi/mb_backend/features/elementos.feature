Feature: Elementos

    As usuario comum
    I want ver todos aas entidades comunitarias de determinada comunidade
    Then visualizar uma determinada entidade comunitaria

    Scenario: Visualizar todas aas entidades comunitarias criadas em uma determinada comunidade
    
        When eu digito o id da comunidade
        Then eu verei todos os elementos criados na comunidade

        When eu digito o id do elemento
        Then eu serei capaz de ver as informacoes
