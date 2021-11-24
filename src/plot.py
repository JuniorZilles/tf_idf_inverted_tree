import matplotlib.pyplot as plt

POINTS = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


def plot_graphics(measures: dict):
    """
    Gera os gráficos
    args:
        measures:dict {
            "precion": precision, "recall": recall, 
            "f_measure": f_measure, "avg_prec": avg_prec, 
            "recall_list": recall_list, "precision_list": precision_list
        }
    """
    interpolated_precision = build_interpolated_list(
        measures['precision_list'])
    eleven_point = build_eleven_point_list(
        interpolated_precision, measures['recall_list'])
    plot_single(measures['precision_list'],
                measures['recall_list'], "blue", ':', "Completa")

    plot_single(interpolated_precision,
                measures['recall_list'], "red", '--', "Interpolada")

    plot_single(eleven_point, POINTS, "green", '-.', "Interpolada 11 pts")

    plot_all(measures['recall_list'], measures['precision_list'],
             interpolated_precision, eleven_point)


def calculate_area_under_curve(x, y):
    """
    Aplicando a Regra dos trapézios 
    args:
        x:list -> pontos de recall
        y:list -> pontos de precision
    returns:
        area abaixo da curva
    """
    #area = np.trapz(y=y, x=x)
    area = 0
    for i in range(1, len(x)):
       h = x[i] - x[i-1]
       area += h * (y[i-1] + y[i]) / 2
    return area


def build_eleven_point_list(precision: list, recall: list) -> list:
    """
    Constroi a lista de precisões de onze pontos, onde a precisão escolhida é sempre a que o recall é maior ou igual ao ponto
    args:
        precision:list -> lista das precisões interpoladas
        recal:list -> lista das revocações

    returns:
        lista de precisões em 11 pontos
    """
    eleven_prec = []
    pos = 0
    for p in POINTS:
        if pos < len(recall) -1:
            while recall[pos] < p:
                pos += 1
        else:
            pos +=1
        if pos + 1 >= len(precision):
            eleven_prec.append(0.0)
        else:
            eleven_prec.append(precision[pos])
    return eleven_prec


def build_interpolated_list(precision: list):
    """
    Calcula as precisões interpoladas
    args:
        precision:list -> lista das precisões
    """
    interpoleted = []
    for i in range(len(precision)):
        interpoleted.append(max(precision[i:]))
    return interpoleted


def plot_single(precision: list, recall: list, color: str, line_style: str, line_label: str) -> None:
    """
    Gera o gráfico
    args:
        precision:list -> lista das precisões
        recal:list -> lista das revocações
        color:str -> cor da linha
        line_style:str -> estilo da linha
        line_label:str -> label da linha
    """

    plt.title("Recall vs. Precision")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.ylim(bottom=0, top=1.03)
    plt.xlim(left=0, right=1.03)
    plt.plot(recall, precision, color=color, ls=line_style, label=line_label)
    plt.grid(True)
    plt.legend()
    plt.xticks(POINTS)
    plt.yticks(POINTS)
    plt.show()
    area = calculate_area_under_curve(recall, precision)
    print(f"AUC {line_label} = {area}")


def plot_all(rec_compl: list, prec_compl: list, prec_interp: list, prec_eleven_points: list) -> None:
    """
    Gera o gráfico
    args:
        rec_compl:list -> lista das precisões completas
        prec_compl:list -> lista das revocações completas
        prec_interp:list -> lista de precisões interpoladas
        prec_eleven_points:list -> lista de precisões em 11 pontos
    """
    plt.title("Recall vs. Precision")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.ylim(bottom=0, top=1.03)
    plt.xlim(left=0, right=1.03)
    plt.plot(rec_compl, prec_compl, color="blue", ls=':', label="Completa")
    plt.plot(rec_compl, prec_interp, color="red", ls='--', label="Interpolada")
    plt.plot(POINTS, prec_eleven_points, color="green",
             ls='-.', label="Interpolada 11 pts")
    plt.grid(True)
    plt.legend()
    plt.xticks(POINTS)
    plt.yticks(POINTS)
    plt.show()
