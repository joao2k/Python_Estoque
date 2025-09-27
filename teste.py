from Modelo import ModeloBase
teste = ModeloBase.DB()


print(teste.insert("""INSERT INTO `fornecedor` (
    `nome`, `cep`, `enredeco`, `num`, `id_estado`, `complemento`, `pessoa_contato`, `numero_contato`, `telefone`
) VALUES (
    'Fornecedor Exemplo',      -- nome (string)
    '12345-678',               -- cep (string)
    'Rua das Flores',          -- enredeco (string)
    100,                       -- num (número)
    5,                         -- id_estado (número)
    'Apto 202',                -- complemento (string)
    'João Silva',              -- pessoa_contato (string)
    '9999-8888',               -- numero_contato (string)
    '11 98765-4321'            -- telefone (string)
);"""))