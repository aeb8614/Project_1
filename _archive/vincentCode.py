import vincent
vincent.core.initialize_notebook()

# Creating a stacked bar chart based on straight count
stack = vincent.StackedBar(alc_count_df)
stack.axis_titles(x='State', y='Count (unadjusted for population)')
stack.legend(title='Alcohol Type')
#stack.colors(brew="Spectral")
stack.display()
plt.savefig("count_stacked.png")


# Creating a stacked bar chart based on adjusted count
stack2 = vincent.StackedBar(alc_person_df)
stack2.axis_titles(x='State', y='Count (adjusted for population)')
stack2.legend(title='Alcohol Type')
#stack2.colors(brew="Spectral")
stack2.display()
stack2.figure.savefig("adj_count_stacked.png")
plt.show()