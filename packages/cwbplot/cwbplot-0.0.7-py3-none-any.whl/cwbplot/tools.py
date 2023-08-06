import math
import numpy as np
import pandas as pd
import datetime as dt
import cwbplot

def cross2d(M, index_i, index_j, theta):
    """cross2d(2darray, array_index_i, array_index_j, math_degree)"""
    slope = math.tan(math.radians(theta))
    i_series = list()
    j_series = list()
    if abs(slope) <=1:
       for j in reversed(range(index_j)):
          i = index_i + round((j - index_j)*slope)
          if i>=M.shape[0]-1 or i<=0: break
          i_series.append(i)
          j_series.append(j)
       for j in range(index_j,M.shape[1]):
          i = index_i + round((j-index_j)*slope)
          if i>=M.shape[0]-1 or i<=0: break
          i_series.append(i)
          j_series.append(j)
    elif abs(slope)>1:
       for i in reversed(range(index_i)):
          j = index_j + round((i-index_i)/slope)
          if j>=M.shape[1]-1 or j<=0: break
          i_series.append(i)
          j_series.append(j)
       for i in range(index_i,M.shape[0]):
          j = index_j + round((i-index_i)/slope)
          if j>=M.shape[1]-1 or j<=0: break
          i_series.append(i)
          j_series.append(j)
    return i_series,j_series


def stnlatlon_stnij(data_lon, data_lat, stn_lon, stn_lat,mask=None,mask_value=0):
  """ how to use:stnlatlon_stnij(mesh_lon,mesh_lat,stn_lon, stn_lat) return index sequence 
       1D and 2D mesh grid is OK 
       mask is the array size same as data_lon and data_lat
       mask_value is the value not be calulated"""
  dist=np.sqrt((data_lat-stn_lat)**2+(data_lon-stn_lon)**2)
  if mask is None:
    indexs = np.unravel_index(np.argmin(dist), dist.shape)
    return indexs
  else:
    mask=np.array(mask)
    #surrounding_points=np.argsort(dist)[:4]
    surrounding_points=np.argsort(np.ravel(dist))[:4]
    for point in surrounding_points:
       indexs=np.unravel_index(point, dist.shape)
       if mask[indexs]!=mask_value:                   
          return indexs  
    ## if not found data in mask return the nearest point
    print('Not found in mask near',stn_lon,stn_lat,'returning nearest point')
    indexs=np.unravel_index(surrounding_points[0], dist.shape)
    return indexs     

def read_xml_cwb(data_time_str,var_list,prefix=''):
  """  read_xml_cwb(data_time_str,var_list,prefix='')
     data_time_str: string format(YYYYMMDDHHNN) in UTC
  """     
  import xmltodict as xmld
  import datetime   as dt
  import pandas as pd
  
  data_time = dt.datetime.strptime(data_time_str, "%Y%m%d%H%M")
  var_name_list=var_list.split()
  ##Reading data
  station_dict={}
  #xml_dir='/IFS6/data2/datarfs/c164/WBGT_OP/STA_DATA/'
  xml_dir='/IFS6/data2/datawrf/obsget/STA_DATA/'
  himawari_dir='/home/c164/web/'
  files=[xml_dir+data_time_str+'.QPESUMS_METRO_STATION.10M.RAD.xml',
         xml_dir+data_time_str+'.QPESUMS_AUTO_STATION.10M_RAD.xml']
  for filename in files:
    with open(filename,encoding='utf-8') as fd:
        doc =xmld.parse(fd.read())
        for j in range(len(doc['cwbopendata']['location'])):
            station_data=doc['cwbopendata']['location'][j]
            single_station_dict={}
            single_station_dict.update({'lat':float(station_data['lat_wgs84']),
                                        'lon':float(station_data['lon_wgs84'])})
            for i in range(len(station_data['weatherElement'])):
              try:
                  '''
                  if (station_data['weatherElement'][i]['elementName']=='WDIR' or
                      station_data['weatherElement'][i]['elementName']=='WDSD'):
                  '''
                  for var_name in var_name_list:
                      if (station_data['weatherElement'][i]['elementName']==var_name):
                        single_station_dict.update({prefix+station_data['weatherElement'][i]['elementName']:
                        float(station_data['weatherElement'][i]['elementValue']['value'])})
              except:
                  pass
  
            if all(x>-99 for x in single_station_dict.values() ):
               station_dict.update({station_data['stationId']:single_station_dict})
  ###convert to dictionary format
  data= pd.DataFrame.from_dict(station_dict,orient='index')
  return data

def stnlatlon_stnij_WGS84(data_lon, data_lat, stn_lon, stn_lat,mask=None,mask_value=0):
  """ how to use:stnlatlon_stnij(mesh_lon,mesh_lat,stn_lon, stn_lat) return index sequence
       1D and 2D mesh grid is OK
       mask is the array size same as data_lon and data_lat
       mask_value is the value not be calulated"""

  import pyproj
  g = pyproj.Geod(ellps='WGS84')
  dist=np.sqrt((data_lat-stn_lat)**2+(data_lon-stn_lon)**2)
  ## finding nearset 4four point index in fatten index  
  nearby_points=np.argsort(np.ravel(dist))[:4]
  
  ## finding ij index of points  (nearby_index)  
  nearby_indexs=(np.unravel_index(nearby_points,dist.shape))

  ## getting data array for corresponding points  
  mesh_stn_lon=np.full(nearby_points.shape,stn_lon)  
  mesh_stn_lat=np.full(nearby_points.shape,stn_lat)  
  ## calculate distance using greate circle distance  
  if type(data_lon).__name__ == 'DataArray':
      _,_,gdist=g.inv(data_lon.data[nearby_indexs],data_lat.data[nearby_indexs] \
                     ,mesh_stn_lon,mesh_stn_lat)
  elif type(data_lon).__name__ == 'ndarray':
     _,_,gdist=g.inv(data_lon[nearby_indexs],data_lat[nearby_indexs] \
                     ,mesh_stn_lon,mesh_stn_lat)
  gdist=np.array(gdist)

  ## resorting the great circle distance(shape=4), returning index 
  g_points=np.argsort(gdist)

  if mask is None:  
    index = np.unravel_index(nearby_points[g_points[0]], data_lon.shape)
    return index
  else:
    mask=np.array(mask)
    for point in g_points:
       index=np.unravel_index(nearby_points[point], data_lon.shape)
 
       if mask[index]!=mask_value:
          return index
    ## if not found data in mask return the nearest point
    print('Not found in mask near',stn_lon,stn_lat,'returning nearest point')
    min_indexs=np.unravel_index(nearby_points[g_points[0]],data_lon.shape)
    return index
  
def read_nc_with_latlonpd(data_time_str,df,nc_path,var_list,prefix='Model',layer=0):
    ''' pandas colums require lon lat info 
    '''
    import netCDF4 as nc
    import datetime as dt
    from wrf import getvar
    if  isinstance(data_time_str,dt.datetime):
        print('detect datetime format')
        data_time=data_time_str
    else:    
        print('detect string format')
        data_time = dt.datetime.strptime(data_time_str, "%Y%m%d%H%M")
    f_name=dt.datetime.strftime(data_time, "wrfout_d02_%Y-%-m-%d_%H:%M:%S")
    print('reading IO')
    nc_fid=nc.Dataset(nc_path+f_name,'r')
    print('end reading IO')
    var_name =var_list.split()
    for var in var_name:
        try:
            if ("Z" in getvar(nc_fid,var).MemoryOrder):
               data=getvar(nc_fid,var)[layer].data
            else:
                data=getvar(nc_fid,var).data
        except:
             pass
     #### convert model to obs format       
        if var=='WDSD':     data=getvar(nc_fid,'uvmet10_wspd_wdir')[0].data
        if var=='WDIR':     data=getvar(nc_fid,'uvmet10_wspd_wdir')[1].data  
        if var=='TEMP':     data=getvar(nc_fid,'T2')[:].data
        if var=='HUMID':    data=getvar(nc_fid,'rh2')[:].data         
        if var=='DD_GRM10': data=getvar(nc_fid,'SWDOWN')[:].data      
        if var=='ELEV':     data=getvar(nc_fid,'ter')[:].data  
        if var=='PRES':    data=getvar(nc_fid,'pressure')[0].data   
            
        if not prefix+'ij' in df.columns:
           #AAdf[prefix+'ij']=df[['lon','lat']].apply(lambda x: tools.stnlatlon_stnij_WGS84 \
           #AA     (data.XLONG,data.XLAT,x[0],x[1],mask=getvar(nc_fid,'XLAND')[:]),axis=1)
           df[prefix+'ij']=df[['lon','lat']].apply(lambda x: stnlatlon_stnij_WGS84 \
                (getvar(nc_fid,'XLONG'),getvar(nc_fid,'XLAT'),\
                 x[0],x[1],mask=getvar(nc_fid,'XLAND')[:]),axis=1)
           #df[prefix+'_ij']=df[['lon','lat']].apply(lambda x: stnlatlon_stnij \
           #     (data.XLONG,data.XLAT,x[0],x[1]),axis=1)
        #AAdf[prefix+var]=df[prefix+'ij'].apply(lambda row: data.d ata[row])
        df[prefix+var]=df[prefix+'ij'].apply(lambda row: data[row])
    return df 

def DMSXYDIM(WXX):
    ''' function for return xdim,ydim at once
        EX: xdim,ydim=cwbplot.tools.DMSXYDIM("WF02")
    '''
    if WXX=='WD01': xdim,ydim=661,385
    if WXX=='WD02': xdim,ydim=1158,673
    if WXX=='WF02': xdim,ydim=263,303
    if WXX=='WE01': xdim,ydim=450,450
    return xdim,ydim

def DMSTAIL(WXX):
    ''' function for return tail of DMSKEY in string format
    '''
    domain2grid={"WD01":"0254485" ,"WD02":"0779334" ,"WF02":"0079689","WD03":"0729136","WE01":"0202500"}
    return domain2grid[WXX]

def DMSLONLAT(WXX,reshape=False, order="F"):
    ''' function for return DMSKEY LON/LAT array at once
        if reshape=True return (xdim,ydim) array)
        EX: dms_lon, dms_lat = cwbplot.tools.DMSLONLAT("WF02",reshape=True)
    '''
    #dmslatlon_path='/home/c052/Pub/anaconda3/envs/plotenv/lib/python3.6/site-packages/cwbplot/sharedata/'
    dmslatlon_path= cwbplot.__path__[0] + "/sharedata/"
    domain2grid={"WD01":"0254485" ,"WD02":"0779334" ,"WF02":"0079689","WD03":"0729136","WE01":"0202500"}
    xdim,ydim = DMSXYDIM(WXX)


    dms_lat   = np.fromfile(dmslatlon_path+'X00LAT'+WXX+'H'+DMSTAIL(WXX),dtype='>d',count=-1,sep="") #LAT
    dms_lon   = np.fromfile(dmslatlon_path+'X00LON'+WXX+'H'+DMSTAIL(WXX),dtype='>d',count=-1,sep="") #LON

    if reshape==True:
       if order == "F":
           data_lat = np.reshape(dms_lat, (xdim,ydim), order=order)
           data_lon = np.reshape(dms_lon, (xdim,ydim), order=order)
       elif order == "C":
           data_lat = np.reshape(dms_lat, (ydim,xdim), order=order)
           data_lon = np.reshape(dms_lon, (ydim,xdim), order=order)
       return data_lon,data_lat
    else:
       return dms_lon,dms_lat
def DMSRESHAPE(var,WXX):
    ''' function for reshape data
        EX: reshape_var = cwbplot.tools.DMSRESHAPE(var,'WF02')
    '''
    xdim,ydim = DMSXYDIM(WXX)
    reshape_var = np.reshape(var, (xdim,ydim), order='F')
    return reshape_var
def Caldtg(dtg,hr):
    if type(dtg).__name__ == 'datetime':
       data_time=dtg
       return dtg+dt.timedelta(hours=hr)
    else:
       try:
         data_time = dt.datetime.strptime(str(dtg),"%Y%m%d%H")+dt.timedelta(hours=hr)
         dt_format="%Y%m%d%H"
       except: 
         data_time = dt.datetime.strptime(str(dtg),"%y%m%d%H")+dt.timedelta(hours=hr)
         dt_format="%y%m%d%H"
       return dt.datetime.strftime(data_time,dt_format) 



def GETPROJ(model, domain, lon=False, lat=False, res='l',dms=False):
    from mpl_toolkits.basemap import Basemap
    WRFM04d01=[ 120.0, 27.065534591674805, 10.0, 40.0]
    WRFM04d02=[ 120.0, 27.065534591674805, 10.0, 40.0]
    WRFM05d01=[ 120.0, 27.065534591674805, 10.0, 40.0]
    WRFM05d02=[ 120.0, 27.065534591674805, 10.0, 40.0]
    RWRFM01d01=[ 120.0, 21.494176864624023, 10.0, 40.0]
    lcc = pd.DataFrame([WRFM04d01,WRFM04d02,WRFM05d01,WRFM05d02,RWRFM01d01],\
                    columns =["lon0","lat0","lat1","lat2"],\
                    index=["wrfm04wd01","wrfm04wd02","wrfm05wd01","wrfm05wd02","rwrfm01we01"])
    cwbplotpath = cwbplot.__path__[0]
    idx = model.lower() + domain.lower()
    lon0, lat0 = lcc.loc[idx]["lon0"], lcc.loc[idx]["lat0"]
    lat1, lat2 = lcc.loc[idx]["lat1"], lcc.loc[idx]["lat2"]
    if dms:
        if idx == "wrfm04wd01":
            lon, lat = np.load(f"{cwbplotpath}/lonlatinfo/WRFM04D01LONLAT.npy")
        elif idx == "wrfm04wd02" or idx == "wrfm04wf02":
            lon, lat = np.load(f"{cwbplotpath}/lonlatinfo/WRFM04D02LONLAT.npy")
        elif idx == "rwrfm01we01":
            lon, lat = np.load(f"{cwbplotpath}/lonlatinfo/RWRFLONLAT.npy")
        if idx == "wrfm04wf02":
            idx = "wrfm04wd02"
        wrfproj = Basemap(projection="lcc", resolution = res, rsphere = 6370000., \
            lon_0 = lon0, lat_0 = lat0, lat_1 = lat1, lat_2 = lat2, \
            llcrnrlat = lat[0,0], \
            llcrnrlon = lon[0,0], \
            urcrnrlat = lat[-1,-1], \
            urcrnrlon = lon[-1,-1])
    else:
        if lon and lat:
            wrfproj = Basemap(projection="lcc", resolution = res, rsphere = 6370000., \
               lon_0 = lon0, lat_0 = lat0, lat_1 = lat1, lat_2 = lat2, \
               llcrnrlat = lat[0,0], \
               llcrnrlon = lon[0,0], \
               urcrnrlat = lat[-1,-1], \
               urcrnrlon = lon[-1,-1])
        else:
            print("Not dms format file, need lon and lat info")
    return wrfproj
   
                                                                
