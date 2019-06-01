The-Hawk-Dove-game-with-Mesa2

https://the-hawk-dove-game-with-mesa2.herokuapp.com/

Los animales necesitan recursos, como agua y alimento, para vivir. En un ambiente favorable un individuo puede tener más hijos que en un ambiente desfavorable, por ejemplo, supongamos, que en un ambiente favorable un individuo tiene en promedio 5 hijos y en un ambiente desfavorable tiene 2 hijos, podríamos asignarle al recurso un valor de 3 puntos, la diferencia entre la cantidad de hijos que tiene el individuo en un ambiente favorable menos la diferencia de hijos que el individuo tiene en un ambiente desfavorable. Los individuos van sumando puntos, cada recurso aporta una pequeña fracción, y cuando llega a una determinada edad el individuo se reproduce asexualmente, crea copias de sí mismo de acuerdo a la cantidad de puntos obtenidos, y luego muere.

Las plantas no se dejan comer, producen sabores desagradables, los animales tampoco se dejan comer, las gacelas evolucionan para correr más rápido, haciéndoles hacen cada vez la vida más difícil a los leones. En este modelo no vamos a considerar  la carrera armamentística asimetría entre presas y depredadores, ni como la vista de los pájaros evoluciono para ver a insectos que se camuflaba y mimetizaban cada vez mejor en el ambiente. Nosotros vamos a suponer que en cada posición del tablero,  el ambiente donde se desarrolla el juego, hay recursos que los animales necesitan para vivir.

Un recurso se puede compartir. Si bien hay situaciones en las cuales a los individuos no les conviene compartir un recurso, por ejemplo si un ambiente favorable tiene para el animal 10 puntos, y un ambiente menos favorable tiene 8 puntos, a nadie le convendría compartir y tener  5 putos. En este modelo supondremos que los recursos son divisibles y que a los animales les conviene compartir. 

Un conflicto se produce cuando dos individuos quieren el mismo recurso. Los conflictos se pueden resolver en forma pacífica, compartiendo el recurso, o escalando, peleando hasta que uno de los dos queda gravemente lesionado.   Las lesiones producidas en un combate entre dos animales son costosas, también es un costo, aunque menor, el tiempo perdido amenazando al contrincante, gruñendo o mostrándole los dientes.

La peleas entre animales se parecen más a una guerra de desgaste asimétrica  que a un juego de halcones y palomas. En una guerra de desgaste ambos contrincantes, el ganador y el perdedor,  pagan el mismo costo, la menor cantidad de golpes que estaba dispuesto a recibir el perdedor.  Por ejemplo, supongamos que un contrincante está dispuesto a pelear hasta que tenga el ojo en compota y el rival hasta las costillas rota. Empieza la pela, un contrincante tira un puño y le rompe el tabique nasal, como los contrincantes son físicamente iguales, el otro tira en puño y le rompe el tabique nasal al otro. Así hasta que llegan a los ojo en compota, momento en que uno de los contrincantes se retira y el otro gana. En este caso gana el animal que estaba dispuesto a pelear hasta tener una costilla rota y ambos animales pagan el costo de romperse el tabique nasal.  Este no es el modelo implementado, el modelo que implemente,  halcones y palomas, solo el perdedor paga un costo fijo y el ganador obtiene el recurso sin resultar lesionado.

Sabemos que el altruismo puede evolucionar si un individuo puede reconocer a individuos altruistas y ayudar solo a los que reconoció como altruista, si un individuo altruista se tira a un rio para salvar 10 individuos el altruistas podría morir, pero el gen para altruismo podría evolucionar si salvo a 10 individuos. De igual manera la cooperación puede evolucionar en un dilema del prisionero repetido, si hay reconocimiento individual de los miembros de la población cooperar si el contrincante colaboro con migo en el paso y desertar si deserto. Estos los casos, altruismo y cooperación, los modelos suponen reconocimiento individual y memoria. En el modelo que  implemente no hay reconocimiento, ni memoria, el individuo son anónimos, no saben, antes de comenzar la pelea si el oponente es violento o pacifico, y tampoco queda recuerdo en la memoria de combate con el individuo.

La cantidad de hijos que un padre tiene depende de los recursos y las lesiones sufridas. Los individuos viven una determinada edad se reproducen y luego mueren, por ejemplo pueden vivir 6 pasos de simulación  dejar 2 hijos. Los hijos son iguales que sus padres, son clones de sus padres ya que en el modelo la reproducción es asexual, heredan la misma forma de resolución de conflictos.  Si los padres resolvían los conflictos compartiendo, los hijos van a compartir, si los padres resolvían las disputas peleando los hijos van a resolver las disputas peleando. El final del juego habrá más individuos que compartan y más individuos violentos.

La explosión demográfica es un problema en la simulación. En la naturaleza las poblaciones no crecen hasta quedarse sin recurso. Si en la simulación hacemos que los individuos más aptos tengan más de 2 hijos el crecimiento es exponencial y en pocas generaciones se produce una sobrepoblación. En cambio si hago que los individuos más aptos tengan un solo hijo, y los menos aptos no tengan ningún hijo,  en cada generación se va reduciendo. Los biólogos propusieron varias explicaciones. Una explicación es selección de grupo, los individuos se reúnen, hacen un censo y se decide, inconscientemente, cuantos descendientes se tendrá en la próxima generación. Otra solución, más realista, es pensar en un problema de optimización. Tener un hijo tiene un coste y solo se obtiene una ganancia si el hijo  llega sano y salvo a la edad adulta y le dé nietos. En la población hay individuos que están genéticamente programados para tener 20 hijos, hay individuos que están programados para temes 10 y los hay que tiene 5 hijos. Si un individuos pone 20 huevos y no puede alimentar a todos, todos mueren y deja menos descendía de alguien que solo pone 5 huevos y los 5 hijos llegan a la edad adulta. Esto da como resultado una regulación dinámica de la cantidad de hijos óptimos.  Para esta simulaciones se implementó una política centralizada, se cuanta la cantidad total de individuos de la población y en base a esto se decide cuantos hijos tendrán en la próxima generación los más aptos y cuantos hijos tendrán los menos aptos.

Primero veremos qué pasa cuando todos los individuos son exactamente iguales, lo único que se diferencian es en la estrategia para resolver conflicto, compartir o pelear. Después analizaremos que pasa cuando los animales se diferencian en algo arbitrario, como el color de cabello o si tienen barba, cosas que no influyen en la fuerza física, ni en la capacidad de lucha e introduciremos estrategias condicionales, como pelear si mi oponente tiene el cabello más oscuro que el mío y compartir en caso contrario. Por ultimo veremos qué pasa cuando los individuos se diferencian en atributo que influye en la fuerza o en  la capacidad de lucha, que pasa con individuos que luchan si mi contrincante es más fuerte y huyen si es alguien más débil.

Compartir o pelear en población donde todos los individuos son iguales
En el primer modelo que implementamos suponemos que todos los individuos son exactamente iguales, no se diferencian en nada, hasta que surge un conflicto. Unos resuelven los conflictos compartiendo y otros peleando.    No sabe qué estrategia va a usar el oponente hasta que empiece el combate. No puede haber estrategia del tipo altruista, si mi oponente es de los que comparten yo voy a compartir, porque no hay forma de saber que hará el oponente. Tampoco puede haber estrategia de tipo colaborativa, si mi oponente compartió en el pasado voy a compartir, no hay discriminación individual, no sé si  tuve un conflicto anterior con el mismo oponente, ni se cómo se comportó en disputas anteriores. 

Todos los individuos ante un conflicto comparten o pelean. Las estrategias son hereditarias. Los individuos que comparten tuvieron un padre que compartía y los individuos que pelean tuvieron un padre que peleaba. Una de las estrategias es compartir. Se comparte si el otro también quiere compartir,  si el otro no quiere compartir, quiere pelear por el recurso, el que quiere compartir le cede el recurso al violento. La otra estrategia pelear, pelea hasta conseguir el recurso y hasta quedar gravemente lesionado.  Si elijo pelear y el otro elije pelear se da una pelea y dado que somos iguales físicamente se tiene el 50% de probabilidades de ganar y 50% de probabilidades de terminar gravemente lesionado.  

Veremos si al final de los juegos hay más individuos que resuelven sus conflictos a los golpes o deciden compartir.  Qué pasa si en una población donde todos comparten se agrega un violento? Puede invadir la población? Que pasa con una población donde todos son violentos y se agrega uno que comparte? 

Todo depende del valor del recurso y del coste de la lesión. Si el valor del recurso es superior al costo de lesión una población violenta no puede ser invadido por alguien que comparta y si en la población inicial todos están compartiendo y se agrega un violento, el violento invade la población y toda la población se vuelve violenta al final de juego.

Por ejemplo, si todos los individuos eligieron pelear y el costo de lesión es superior al valor del recurso a mí me conviene elegir compartir, porque si bien mi ganancia neta va a ser 0, voy a ceder con todos, no voy a ganar nunca, si elijaría pelear la mitad de las veces ganaría y la otra mitad de las veces perdería, la mitad de las veces obtendría el recurso y la otra mitad de las veces quedaría lesionado, y dado que la lesión es mayor que el beneficio del recuso, obtendría en promedio un resultado menor que cero.

En resumen, si valor del recurso es mayor que el costo de perder una pelea y tengo una población pacifica con solo agregar un individuo violento, que en vez de compartir prefiera pelear, al final del juego todos los individuos van a ser violentos. Si el valor del recurso es menor que el costo de lesiones al final del juego voy a tener en la población un porcentaje de sujetos que prefieren compartir y un porcentaje de violentos, mientras mayor sea el costo por perder una pelea mayor va a ser el porcentaje de la población que va a preferir ser pacífica y compartir recursos en conflicto. Una conclusión interesante es que por más grande que sea el coste de lesión siempre habrá un pequeño porcentaje que le rendirá ser violento. 


Estrategias condicionales usando diferencias arbitrarias entre los individuos

En la vida real no somos clones, no somos todos iguales, hay diferencias arbitrarias, como el color de pelo, que no influyen en el resultado de una pelea y hay diferencias entre los individuos, como fuerza física o tamaño que si influye en resultado de un combate. Primero vamos a considerar diferencias en atributos no influyen en el resultado de un combate, como tener barba verde,  cabello oscuro, piel clara. Luego vamos a considerar diferencias que si influyen en el resultado de una pelea, como ser más grande y más fuerte.

Supongamos que hay individuos que tienen cabello claro y hay individuos con cabello oscuro, además suponemos que cada individuo sabe su color de cabello y puede ver el color de cabello de su oponente, pero no puede saber si su oponente va a estar dispuesto a compartir el recurso o va a pelear. 

En un punto anterior se explicó el altruismo, un individuo se arroja al rio y muere pero logra salvar a 10 individuos altruistas, con individuos que pueden reconocer a individuos altruistas y tienen una estrategia condicional del tipo “si el que se está ahogando es un individuo altruista tirarse al rio e intentar salvarlo. En este caso no podemos tener una estrategia del tipo “comparto solo con los individuos que comparten” porque no hay indicios de si es pacífico o violento, antes de que empiece la pelea no sé sabe cómo se comportara el oponente. 

En un punto anterior también se explicó que puede surgir la cooperación en un dilema del prisionero repetido, cuando hay reconocimiento individual, memoria de encuentros anteriores y una estrategia condicional del tipo “compartir si en oportunidades anteriores el individuo compartió y desertar en caso contrario”. En el juego que estamos considerando no hay reconocimiento individual, ni memoria de conflictos pasados. Esto se puede deber a que no tengan memoria, o a que sea muy raro que dos individuos se vuelvan a encontrar en el futuro, como pueden ser un conflicto entre dos desconocidos en una gran ciudad.

Los animales pueden usar diferencias arbitrarias para resolver conflictos. Además de las estrategias simples,   siempre compartir, siempre pelear, vamos a   agregar una tercera estrategia, una estrategia condicional,  “pelear solo si mi contrincante tiene el cabello más oscuro que mi color de cabello y compartir en caso contrario”. Que sucederá en este caso? qué estrategia me conviene a mí adoptar para ganar más puntos? Si vas a roma has le de los romanos, si todos están usando la estrategia condicional me conviene hacer lo que todos hacen?

Sabemos que si el recurso vale más que el costo de una lesión conviene pelear y que si el costo de una lesión es mayor de que valor del recurso lo que conviene hacer depende de lo que está haciendo la población,  va a haber un porcentaje de la población que comparta y otro que pelee, el porcentaje depende del valor del recurso y del costo de lesión, a mayor costo de lesión menor cantidad de individuos van pelear. Ahora veremos qué pasa cuando agregamos una estrategia condicional que depende de una diferencia arbitraria que hay entre los individuos.

Se puede ver en la simulación que si todos los individuos están usando la estrategia condicional “si mi oponente tiene el cabello más oscuro que el mío entonces pelear, en caso contrario compartir” y el valor del recurso es menor que el costo de una lesión, ninguna otra estrategia puede invadir esa población.


Diferencias entre individuos en aspectos que influyen en el resultado de una pelea
Ahora consideremos una población donde los individuos son distintos, pero en aspectos que influyen en el resultado de una pelea, por ejemplo la fuerza y el tamaño. En la población hay individuos grandes y fuertes e individuos pequeños y débiles. Al igual que en los casos anteriores, los individuos no saben cómo reaccionara el oponente, si estará dispuesto a compartir o tendrá ganas de pelear. Solo se que el animal es más grande, o más chico, no sé si está dispuesto a atacarme o podemos compartir el recurso. 

Un ejemplo de asimetría puede ser el tamaño, hay individuos grandes e individuos chicos, otro ejemplo puede ser el sexo, hay individuos que son machos y otros que son hembras. Para simplificar asumamos que la asimetría puede tener solo dos valores, por ejemplo grande o chico, no hay individuos más o menos grandes, ni individuos que pesen 62 kg y otros que pesen 6 5kg, solo podemos clasificar a los individuos en grandes o chicos. En una pelea entre dos individuos grandes existe la misma probabilidad de que gane uno o de que gane el otro, igualmente una pelea entre individuos chicos tenemos el 50% de probabilidad de que gane uno o de que gane el otro. Pero cuando se enfrenta un individuo grande contra un individuo chico la probabilidad de que gane el más grande es un parámetro del modelo. Si queremos que el más grande siempre gane ponemos un porcentaje de 100. Si en peleas entre grandes y chicos el 80% de las veces gana el más grande ajustamos el parámetro del modelo a 80.

En una población asimétrica del tipo que estamos considerando pueden existir cuatro estrategias. Las dos estrategias que teníamos en la población simétrica, Siempre pelear, siempre  compartir, y dos estrategias condicionales, una de sentido común, pelear si mi oponente es de menor tamaño y compartir y caso contrario, y una estrategia condicional paradójica, pelear si mi oponente es más grande y compartir en caso contrario.

No hace falta ser muy inteligente para darte cuenta que sos un individuo grande y los costes de lesión son mayores que el valor del recurso la mejor estrategia es “pelear con los que son más chicos que vos y compartir el recurso en caso contrario”. En una población donde todos golpean a los más débiles no puede ser invadida por ninguna de las otras dos estrategias, siempre pelear, ni por siempre compartir.

Que pasa en una población donde todos los individuos pelean si oponente es más grande y comparten en caso contrario? Puede ser invadido por las estrategias alternativas, siempre pelear, siempre compartir, o pelear solo si mi oponente es menor? Si el costo de lesión es superior al valor del recurso y todos siguen la estrategia paradójica, un individuo que siga la estrategia de sentido común, “pelear solo si el oponente es menor y compartir en caso contrario” no podrá invadir, está en peor situación que alguien que siga una estrategia paradójica, se pelearía con todos, y con un costo de lesión de más de 8 veces el valor del recurso, una probabilidad de ganar del 80% no compensa. 

Si los machos son más fuertes y grandes que las hembras, el 80% de las peleas entre machos y hembras las gana un macho, una estrategia condicional paradójica del tipo si sos hembra y tu contrincante es un macho atacar,  y si sos macho y tu contendiente es una hembra huir podría ser una estrategia evolutivamente estable. Cualquiera que hiciera algo distinto estaría en desventaja, las estrategias siempre huir, siempre pelear, están en desventaja contra la estrategia condicional paradójica que estaría usando la mayoría de la población. Aunque no es fácil decir cómo podría llegar una población a que todos sus miembros adopten una estrategia condicional paradójica, no hay etapas intermedias que sean evolutivamente estables.

Juegos con estrategias evolutivas inestables

Como vimos cuando tratamos el tema de la sobrepoblación, tener 5 hijos no siempre es mejor que tener 2 porque tener un hijo tiene un costo y da puntos cuando el descendiente llega sano y salvo a la edad adulta y da nietos.  En la reproducción sexual los costos de tener un hijo lo puede pagar uno solo de los progenitores o se pueden compartir entre los dos progenitores. Una carrera armamentística produjo diferencias entre los sexos.

Supongamos que tenemos dos tipos de jugadores, machos y hembras, y dos tipos de estrategia para cada uno de los tipos de jugadores. Los machos pueden ser fieles o atorrantes y las hembras pueden ser fáciles y esquivas. Supongamos que la ventaja evolutiva por tener una  cría le da 15 puntos a cada uno de los padres, supongamos que el coste para tener una criar una cría con éxito es de 20 puntos, este coste se puede repartir entre los padres o lo pude pagar solo la hembra dependiendo del tipo de estrategia, supongamos que en un cortejo se pierden 3 puntos.

En un encuentro de macho atorrante con una hembra fácil, le da al macho 15 puntos y a la hembra -5 puntos.
Un encuentro entre un macho fiel y una hembra esquiva, el macho gana 2 puntos, esto es 15 de la cría -10 de la crianza compartida, -3 del cortejo. La hembra también obtiene el mismo puntaje.

Un encuentro entre un macho atorrante y una hembra esquiva cada uno obtiene 0 puntos, no tienen ninguna cría, no hay cortejo, ni hay costo de crianza.
Un encuentro entre un macho fiel y una hembra fácil, el macho consigue 5 puntos y la hembra también consigue 5 puntos.
Si se analiza el juego parecería que hay un equilibrio estable. En la primera edición del Gen Egoísta, Richard Dawkins pensaba que este juego tenía un equilibro  Analizando en profundidad el juego se puede ver que en realidad el equilibrio es inestable, el juego oscila, una vez que se alcanza el equilibrio, si se produce una pequeña modificación en los porcentajes, lejos de autorregularse y volver al equilibrio, el desequilibrio se potencia hasta alcanzar un equilibrio distinto.

Supongamos una población donde todas las hembras son fáciles y todos los machos fieles, si se introduce un macho atorrante este, a diferencia del macho fiel, no paga el coste de la crianza, por lo tanto va a obtener mejores puntajes que un macho fiel y el número de machos atorrantes aumenta.

A medida que los machos atorrantes aumentan, las hembras fáciles empiezan a tener menos ventaja que las hembras esquivas. Cuando la mayoría de los machos son atorrantes, las hembras esquivas obtienen mejor resultado que las hembras fáciles y por lo tanto su número aumenta.

Cuando se llega a unan situación donde todas las hembras son esquivas y los machos atorrantes, un macho fiel puede invadir la población, obtiene mejor desempeño que un macho atorrante.

Si todas las hembras son esquivas y los machos son files, una hembra fácil puede invadir la población y sacar ventaja de que todos los machos son fieles. En este punto estamos en la misma situación que cuando se empezó el ciclo, una población donde las hembras son fáciles y los machos son fieles.


 
