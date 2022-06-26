import twint
#configuration
config = twint.Config()
config.Search= "#jisoo"
config.Image = True
config.Limit = 5
#config.Lang = "en"
config.Min_likes = 5000
config.Images = True
config.Store_csv = True
config.Output = "Jisoo5.csv"
#config.Format = "{id} str({id}) "
twint.run.Search(config)

