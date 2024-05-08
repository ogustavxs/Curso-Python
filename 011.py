larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
print('Sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(larg, altu, larg*altu))
print('Para pintar essa parede, você precisara de {}l de tinta.'.format((larg*altu)/2))