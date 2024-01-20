# API GB E-COMMERCE - PASSO-A-PASSO

## Certifique-se de ter o Docker e Docker Compose instalados

### Inicie a Aplicação com Docker Compose
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker-compose up -d --build</code></pre>
</div>

### Executar Migrações e Criar Superusuário
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker-compose exec api python manage.py makemigrations</code></pre>
</div>
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker-compose exec api python manage.py migrate</code></pre>
</div>

<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker-compose exec api python manage.py createsuperuser --noinput</code></pre>
</div>

### Acessar a API / Swagger
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>http://localhost:8000</code></pre>
</div>

### Acessar GraphQl
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>http://localhost:8000/graphql</code></pre>
</div>

### Acessar Redoc
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>http://localhost:8000/redoc</code></pre>
</div>

### Paginação de Produtos
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>http://localhost:8000/products/?page=1&pagesize=20</code></pre>
</div>

## Testes da API
**Caso queria testar a API no terminal.**

### Testando Todos os casos.
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker exec api python manage.py test</code></pre>
</div>

### Testando Token, Refresh_Token, Verify_Token, Autenticação do usuário.
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker exec api python manage.py test api_ecommerce</code></pre>
</div>

### Testando Product, Reviews Model e Autentição de get sem logar.
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker exec api python manage.py test products</code></pre>
</div>

### Testando Categories, Model e Autentição de get sem logar.
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker exec api python manage.py test categories</code></pre>
</div>

### Testando Suppliers, Model e Autentição de get sem logar.
<div>
  <span class="copy-icon">
    <i class="fas fa-copy"></i>
  </span>
  <pre><code>docker exec api python manage.py test suppliers</code></pre>
</div>


